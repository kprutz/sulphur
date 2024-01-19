from datetime import datetime
import math
import pdb

from .models import Sensors
from .purpleutils import PurpleUtils
from .fileComplaint import fileComplaint


SENSOR_INDEX = 145788
PM25_AQI_LIMIT = 100

class Complainer:
    def complain(self, dry_run=False):
        if dry_run:
            print('This is a dry-run - not submitting complaints')
        lastTime = datetime.timestamp(self.lastScanTime())
        if lastTime:
            now = datetime.timestamp(datetime.now())
            self.scanForComplaints(lastTime, now, dry_run)
            Sensors.objects.create(
                    sensor_index=SENSOR_INDEX,
                    last_complainer_run=datetime.now())
        else:
            print('Could not find last known scan time. Not filing any complaint. Set a last_scan_time in db, then re-run.')

    def lastScanTime(self):
        s = Sensors.objects.last()
        return s.last_complainer_run.replace(tzinfo=None)

    def scanForComplaints(self, start_time, end_time, dry_run):
        sensorData = PurpleUtils.getSensorHistory(SENSOR_INDEX, start_time, end_time)
        # Find all the times when the PM2.5 limit was exceeded - over 35
        incidents = self.findIncidents(sensorData) or []
        print('************************************')
        print('Incidents')
        print(incidents)
        print('************************************')
        for incident in incidents:
            fileComplaint(incident, dry_run)
            # update after each complaint so we don't duplicate submissions if a complaint fails to submit
            if not dry_run:
                Sensors.objects.create(
                    sensor_index=SENSOR_INDEX,
                    last_complainer_run=datetime.now())
        return

    def findIncidents(self, data):
        incidents = []
        currentlyExceeded = False
        incidentStart = 0
        incidentEnd = 0
        incidentPM25s = []
        if not data:
            return
        for datum in data:
            [d_time, d_pm25, d_pm10, d_pm25_aqi] = datum
            print(datum)
            if not currentlyExceeded and d_pm25_aqi > PM25_AQI_LIMIT:
                currentlyExceeded = True
                incidentStart = d_time
                incidentPM25s.append(d_pm25_aqi)
            elif currentlyExceeded and d_pm25_aqi < PM25_AQI_LIMIT:
                incidentEnd = d_time
                if len(incidentPM25s) > 1:
                    print('incidentPM25s')
                    print(incidentPM25s)
                    incidents.append({
                        'start_timestamp': incidentStart,
                        'end_timestamp': incidentEnd,
                        'pm25_avg': math.floor(sum(incidentPM25s) / len(incidentPM25s)),
                        'pm25_max': max(incidentPM25s),
                    })
                # reset counters
                currentlyExceeded = False
                incidentStart = 0
                incidentEnd = 0
                incidentPM25s = []
            elif currentlyExceeded:
                incidentPM25s.append(d_pm25_aqi)
        return incidents

