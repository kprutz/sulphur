'''
Files a citizen complaint on the ldeq website with Cindy's info
'''

from .complainerUtils import *

'''
CONSTANTS
'''

# SITE_URL = "https://www.deq.louisiana.gov/"
# COMPLAINT_FORM_SELECTOR = "#header-1 > div > a:nth-child(4)"
# CITIZEN_COMPLAINT_SELECTOR = "#pagebuilder > div > a:nth-child(1)"
COMPLAINT_FORM_URL = "https://internet.deq.louisiana.gov/portal/ONLINESERVICES/FORMS/FILE-A-CITIZEN-COMPLAINT"
OPTIONAL = True

SOLVERKEY = "2ee4b597258f59049433249fa6e9a4cf"

submitter_data = {
    "first_name": "Cindy",
    "last_name": "l",
    "phone": "2252222222",
    "email": "c@g.com",
    # optional
    "address_street": "123 sesame",
    "city": "Sulphur",
    "state": "Louisiana",
    "zipcode": 72345,
    "request_follow_up": "Yes",
}
site_data = {
    "address_street": "456 hullo",
    "city": "Sulphur",
    "parish": "Calcasieu Parish",
    "description": "06/12/2023",
    # optional
    "alleged_violator": "me",
    "zipcode": 78711,
    "date": "06/12/2023",
    "start_time": "11:30:00",
    "end_time": "3:00:00",
    "media_affected": "air",
    "directions_to_site": "over yonder",
}

def fill_out_form(browser):
    # filling in caller information section
    enterInput(browser, "txtFirstName", submitter_data["first_name"])
    enterInput(browser, "txtLastName", submitter_data["last_name"])
    enterInput(browser, "txtphone", submitter_data["phone"])
    enterInput(browser, "txtemail", submitter_data["email"])
    enterInput(browser, "txtcalleraddress", submitter_data["address_street"])
    enterInput(browser, "txtcallercity", submitter_data["city"])
    selectDropdown(browser, "ddcallerstate", submitter_data["state"])
    enterInput(browser, "txtcallerzip", submitter_data["zipcode"])
    selectDropdown(browser, "ddfollowup", submitter_data["request_follow_up"])

    # filling in site information section
    enterInput(browser, "txtallegedviolator", site_data["alleged_violator"], OPTIONAL)
    enterInput(browser, "txtincidentaddress", site_data["address_street"])
    enterInput(browser, "txtincidentcity", site_data["city"])
    enterInput(browser, "txtincidentzip", site_data["zipcode"])
    enterInput(browser, "txtdateofdis", site_data["date"])
    enterInput(browser, "txtnoticedtimebegan", site_data["start_time"])
    enterInput(browser, "txtnoticedtimeended", site_data["end_time"])
    selectDropdown(browser, "ddincidentparish", site_data["parish"])
    selectDropdown(browser, "ddincidentmediaaffected", site_data["media_affected"])
    enterInput(browser, "txtdescriptionofcomplaint", site_data["description"])
    enterInput(browser, "txtdirectionsforreachingthesite", site_data["directions_to_site"], OPTIONAL)

if __name__ == '__main__':
    complain()
