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
    def getSensorData(sensor_index):
        r = PurpleUtils._makePurpleRequest(sensor_index)
        return PurpleUtils._decodeAndGetData(r)

    @staticmethod
    def getSensorHistory(sensor_index, params):
        r = _makePurpleRequest(sensor_index, True, params=_formatParams(params))
        return _decodeAndGetData(r)

    @staticmethod
    def getSensorHistory_pastWeek(sensor_index, average=30):
        end_time = datetime.datetime.now().timestamp()  # the current timestamp in seconds
        timedelta = datetime.timedelta(7).total_seconds()  # 2 weeks in seconds
        TIME_PARAMS = 'start_timestamp=%d&end_timestamp=%d&average=%d' % (end_time - timedelta,end_time,average)
        r = PurpleUtils._makePurpleRequest(sensor_index, True, params=FIELDS_PARAM + '&' + TIME_PARAMS)
        return PurpleUtils._decodeAndGetData(r)

    @staticmethod
    def _makePurpleRequest(sensor_index, history=False, params=''):
        url = 'https://api.purpleair.com/v1/sensors/' + str(sensor_index) + ('/history' if history else '') + ('?' + params if params else '')
        headers = {'X-API-Key': API_KEY}
        r = requests.get(url, headers=headers)
        return r

    @staticmethod
    def _formatParams(params):
        return '&'.join(['%s=%s' % (item[0], item[1]) for item in params.items()])

    @staticmethod
    def _decodeAndGetData(raw_data):
        data = json.loads(raw_data.content.decode('UTF-8'))
        if not data.get('data'):
            print('Errored:')
            print(data)
            return data
        return data['data']


# end_time = datetime.datetime.now().timestamp()  # the current timestamp in seconds
# timedelta = datetime.timedelta(365).total_seconds()  # 1 year in seconds
# average = 525600 # 1 year in minutes
# TIME_PARAMS = 'start_timestamp=%d&end_timestamp=%d&average=%d' % (end_time - timedelta,end_time,average)
#
# s = getSensorHistory(SENSOR_ID, {
#     'fields': 'pm2.5',
#     'average': 10,
#     'start_timestamp': start_time,
#     'end_timestamp': end_time
#     })
