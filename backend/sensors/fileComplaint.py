import math

from .complainerUtils import *

'''
CONSTANTS
'''

submitter_data = {
    "first_name": "Cindy",
    "last_name": "Robertson",
    "phone": "3378886652",
    "email": "cindy@micah68mission.org",
    # optional
    "address_street": "624 W. Verdine",
    "city": "Sulphur",
    "state": "Louisiana",
    "zipcode": 70663,
    "request_follow_up": "No",
}

site_data = {
    "address_street": "Unknown",
    "city": "Sulphur",
    "parish": "Calcasieu Parish",
    # optional
    "alleged_violator": None,
    "zipcode": None,
    "media_affected": "air",
    "directions_to_site": None,
}

site_by_angle = {
    
}


# start_time, end_time as timestamps
def fileComplaint(incident, dry_run):
    # 'start_timestamp', 'end_timestamp', 'pm25_avg', 'pm25_max'
    site_data['date'] = formatDate(incident['start_timestamp']) # e.g. "06/12/2023"
    site_data['start_time'] = formatTime(incident['start_timestamp']) # e.g. "11:30:00"
    site_data['end_time'] = formatTime(incident['end_timestamp'])

    seconds_over_limit = incident['end_timestamp'] - incident['start_timestamp']
    print('seconds over limit')
    print('{} - {} = {}', incident['end_timestamp'], incident['start_timestamp'], seconds_over_limit)
    hours_over_limit = math.floor(seconds_over_limit / 3600)
    print('hours over limit is {}', hours_over_limit)
    minutes_over_limit = math.floor((hours_over_limit - seconds_over_limit / 3600) * 60)
    print('minutes over limit is {}', minutes_over_limit)
    site_data['description'] = '''My Purple Air monitor logged PM2.5* levels over 100 (the level above which the EPA begins cautioning at-risk groups) for {} hours and {} minutes (from {} to {}) on {}. The average PM2.5 AQI value was {}. The air monitor data can be seen at https://map.purpleair.com/1/mAQI/a10/p604800/cC0?select=145788#12.17/30.22823/-93.3634.\n 
*PM2.5 levels are using the US EPA PM2.5 AQI value'''.format(hours_over_limit, 0, site_data['start_time'], site_data['end_time'], site_data['date'], incident['pm25_avg'])
    if dry_run:
        print('')
        print(site_data)
        return
    complain(submitter_data, site_data)
