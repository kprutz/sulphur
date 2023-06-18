from datetime import datetime

class Complainer:
    def complain(self):
        lastTime = self.lastScanTime()
        if lastTime:
            now = datetime.now().timestamp()
            scanForComplaints(lastTime, now)
        else:
            print('Could not find last known scan time. Not filing any complaint. Set a last_scan_time in db, then re-run.')

    def lastScanTime():
        # TODO - check db for last time we ran the scanner
        return

    def scanForComplaints(start_time, end_time):
        # TODO
        return

