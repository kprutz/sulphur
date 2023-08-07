import requests
import json
import pandas
import datetime


FIELDS_PARAM = 'fields=pm2.5_alt,'
API_KEY = '588EEF1E-F8DC-11ED-BD21-42010A800008'
SENSOR_ID = 145788
PM25_24HR_AVG_LIMIT = 35
PM25_AQI_LIMIT = 150
DAY_AVG = 1440


SENSOR_IDS = [
    {'index': 145800, 'purple_name': "Westlake", 'name': ""},
    {'index': 38421, 'purple_name': "Westlake, Louisiana", 'name': ""},
    {'index': 30131, 'purple_name': "Margaret Place, Lake Charles, Louisiana", 'name': ""},
    {'index': 174173, 'purple_name': "Beauregard Ave Sulphur", 'name': ""},
    {'index': 145788, 'purple_name': "624 W. Verdine, Sulphur", 'name': ""},
]

class PurpleUtils:
    @staticmethod
    def getSensorHistory(sensor_index, start_time_sec, end_time_sec):
        params = {
            'fields': 'pm2.5_atm,pm10.0_atm',
            'average': PurpleUtils._computeAverage(start_time_sec, end_time_sec),
            'start_timestamp': start_time_sec,
            'end_timestamp': end_time_sec
        }
        print('Getting sensor data with params:')
        print(params)
        r = PurpleUtils._makePurpleRequest(sensor_index, True, params=PurpleUtils._formatParams(params))
        return PurpleUtils._decodeAndGetData(r)

    @staticmethod
    def getSensorHistoryForDays(sensor_index, num_days):
        end_time = datetime.datetime.now().timestamp()
        timedelta = datetime.timedelta(num_days).total_seconds()
        return PurpleUtils.getSensorHistory(sensor_index, end_time - timedelta, end_time)

    @staticmethod
    def _computeAverage(start_time_sec, end_time_sec):
        DAY = 24 * 60 * 60  # in seconds
        YEAR = 365 * DAY  # in seconds
        '''
        The desired average in minutes, one of the following:
            Avg                Maximum timedelta 
            0 (real-time)      2 days
            10 (default)       3 days
            30                 7 days
            60                 14 days
            360 (6 hour)       90 days
            1440 (1 day)       1 year
            10080 (1 week)     5 years
            44640 (1 month)    NO LONGER SUPPORTED BY API?
            525600 (1 year)    Any
        '''
        timedelta = (end_time_sec - start_time_sec)
        if (timedelta <= 2 * DAY): return 10   # Could do 0, but for AQI conversion use 10
        if (timedelta <= 3 * DAY): return 10
        if (timedelta <= 7 * DAY): return 30
        if (timedelta <= 14 * DAY): return 60
        if (timedelta <= 90 * DAY): return 360
        if (timedelta <= 1 * YEAR): return 1440
        if (timedelta <= 5 * YEAR): return 10080
        return 525600

    @staticmethod
    def _makePurpleRequest(sensor_index, history=False, params=''):
        url = 'https://api.purpleair.com/v1/sensors/' + str(sensor_index) + ('/history' if history else '') + ('?' + params if params else '')
        headers = {'X-API-Key': API_KEY}
        r = requests.get(url, headers=headers)
        return r

    @staticmethod
    def _formatParams(params):
        # e.g. 'start_timestamp=%d&end_timestamp=%d&average=%d&fields=pm2.5_alt'
        return '&'.join(['%s=%s' % (item[0], item[1]) for item in params.items()])

    @staticmethod
    def _decodeAndGetData(raw_data):
        data = json.loads(raw_data.content.decode('UTF-8'))
        if data.get('error') or not data.get('data'):
            print('Errored:')
            print(data)
            return None
        for datum in data['data']:
            [d_time, d_pm25, d_pm10] = datum
            datum.append(PurpleUtils.aqiFromPM(d_pm25))
        # sort by datetime
        data['data'].sort()
        return data['data']
    
    @staticmethod
    def getSensorData(sensor_index):
        r = PurpleUtils._makePurpleRequest(sensor_index)
        return PurpleUtils._decodeAndGetData(r)
    
    # Convert US AQI from raw pm2.5 data
    @staticmethod
    def aqiFromPM(pm):
        if not float(pm):
            return "-"
        if pm == 'undefined':
            return "-"
        if pm < 0:
            return pm
        if pm > 1000:
            return "-"
        """
                                            AQI   | RAW PM2.5    
        Good                               0 - 50 | 0.0 – 12.0    
        Moderate                         51 - 100 | 12.1 – 35.4
        Unhealthy for Sensitive Groups  101 – 150 | 35.5 – 55.4
        Unhealthy                       151 – 200 | 55.5 – 150.4
        Very Unhealthy                  201 – 300 | 150.5 – 250.4
        Hazardous                       301 – 400 | 250.5 – 350.4
        Hazardous                       401 – 500 | 350.5 – 500.4
        """

        if pm > 350.5:
            return PurpleUtils.calcAQI(pm, 500, 401, 500.4, 350.5)  # Hazardous
        elif pm > 250.5:
            return PurpleUtils.calcAQI(pm, 400, 301, 350.4, 250.5)  # Hazardous
        elif pm > 150.5:
            return PurpleUtils.calcAQI(pm, 300, 201, 250.4, 150.5)  # Very Unhealthy
        elif pm > 55.5:
            return PurpleUtils.calcAQI(pm, 200, 151, 150.4, 55.5)  # Unhealthy
        elif pm > 35.5:
            return PurpleUtils.calcAQI(pm, 150, 101, 55.4, 35.5)  # Unhealthy for Sensitive Groups
        elif pm > 12.1:
            return PurpleUtils.calcAQI(pm, 100, 51, 35.4, 12.1)  # Moderate
        elif pm >= 0:
            return PurpleUtils.calcAQI(pm, 50, 0, 12, 0)  # Good
        else:
            return 'undefined'

    # Calculate AQI from standard ranges
    @staticmethod
    def calcAQI(Cp, Ih, Il, BPh, BPl):
        a = (Ih - Il)
        b = (BPh - BPl)
        c = (Cp - BPl)
        return round((a / b) * c + Il)