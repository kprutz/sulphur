from .purpleUtils import *
import datetime

'''
Checks if we should send a complaint
 - Saves the timestamp when we check to the database
 - Saves whether or not a complaint was created
'''

SENSOR_IDS = [
    {'index': 145800, 'purple_name': "Westlake", 'name': ""}, 
    {'index': 38421, 'purple_name': "Westlake, Louisiana", 'name': ""},
    {'index': 30131, 'purple_name': "Margaret Place, Lake Charles, Louisiana", 'name': ""},
    {'index': 174173, 'purple_name': "Beauregard Ave Sulphur", 'name': ""},
    {'index': 145788, 'purple_name': "624 W. Verdine, Sulphur", 'name': ""},
]

end_time = datetime.datetime.now().timestamp()  # the current timestamp in seconds
timedelta = datetime.timedelta(365).total_seconds()  # 1 year in seconds
average = 525600 # 1 year in minutes
TIME_PARAMS = 'start_timestamp=%d&end_timestamp=%d&average=%d' % (end_time - timedelta,end_time,average)

s = getSensorHistory(SENSOR_ID, {
    'fields': 'pm2.5',
    'average': 10,
    'start_timestamp': end_time - timedelta,
    'end_timestamp': end_time
    })


