'''
Files a citizen complaint on the ldeq website with Cindy's info
'''

import random
import pdb
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions


def enterInput(id, value, optional = False):
    if optional and not value: return
    input_element = browser.find_element(By.ID, id)
    input_element.send_keys(value)
    browser.implicitly_wait(random.randint(1,10))

def selectDropdown(id, value, optional = False):
    if optional and not value: return
    dropdown_element = Select(browser.find_element(By.ID, id))
    dropdown_element.select_by_value(value)
    browser.implicitly_wait(random.randint(1,10))

def captcha():
    xpath = "//iframe[starts-with(@name, 'a-') and starts-with(@src, 'https://www.google.com/recaptcha')]"
    WebDriverWait(browser, 10).until(ExpectedConditions.frame_to_be_available_and_switch_to_it(browser.find_element(By.XPATH, xpath)))
    element = browser.find_element(By.CSS_SELECTOR, "div.recaptcha-checkbox-checkmark")
    WebDriverWait(browser, 20).until(ExpectedConditions.element_to_be_clickable(element))
    browser.implicitly_wait(random.randint(5,10))
    browser.execute_script("arguments[0].click()", element)

SITE_URL = "https://www.deq.louisiana.gov/"
COMPLAINT_FORM_SELECTOR = "#header-1 > div > a:nth-child(4)"
CITIZEN_COMPLAINT_SELECTOR = "#pagebuilder > div > a:nth-child(1)"
# COMPLAINT_FORM_URL = "https://internet.deq.louisiana.gov/portal/ONLINESERVICES/FORMS/FILE-A-CITIZEN-COMPLAINT"
OPTIONAL = True

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

options = Options()
options.browserName = "Chrome"
options.browserVersion = "103.0"
browser = webdriver.Chrome(options=options)

browser.get(SITE_URL)
browser.maximize_window()
browser.find_element(By.CSS_SELECTOR, COMPLAINT_FORM_SELECTOR).click()
browser.find_element(By.CSS_SELECTOR, CITIZEN_COMPLAINT_SELECTOR).click()


captcha()

pdb.set_trace()

# filling in caller information section
enterInput("txtFirstName", submitter_data["first_name"])
enterInput("txtLastName", submitter_data["last_name"])
enterInput("txtphone", submitter_data["phone"])
enterInput("txtemail", submitter_data["email"])
enterInput("txtcalleraddress", submitter_data["address_street"])
enterInput("txtcallercity", submitter_data["city"])
selectDropdown("ddcallerstate", submitter_data["state"])
enterInput("txtcallerzip", submitter_data["zipcode"])
selectDropdown("ddfollowup", submitter_data["request_follow_up"])

# filling in site information section
enterInput("txtallegedviolator", site_data["alleged_violator"], OPTIONAL)
enterInput("txtincidentaddress", site_data["address_street"])
enterInput("txtincidentcity", site_data["city"])
enterInput("txtincidentzip", site_data["zipcode"])
enterInput("txtdateofdis", site_data["date"])
enterInput("txtnoticedtimebegan", site_data["start_time"])
enterInput("txtnoticedtimeended", site_data["end_time"])
selectDropdown("ddincidentparish", site_data["parish"])
selectDropdown("ddincidentmediaaffected", site_data["media_affected"])
enterInput("txtdescriptionofcomplaint", site_data["description"])
enterInput("txtdirectionsforreachingthesite", site_data["directions_to_site"], OPTIONAL)

# captcha
# captcha()

pdb.set_trace()

#
# random_email = str(random.randint(0,99999)) + "@example.com"
#
# password = browser.find_element(By.ID, "input-password")
# password.send_keys("123456")
#
# password_confirm = browser.find_element(By.ID, "input-confirm")
# password_confirm.send_keys("123456")
#
# newsletter = browser.find_element(By.XPATH, value="//label[@for='input-newsletter-yes']")
# newsletter.click()
#
# terms = browser.find_element(By.XPATH, value="//label[@for='input-agree']")
# terms.click()
#
# continue_button = browser.find_element(By.XPATH, value="//input[@value='Continue']")
# continue_button.click()
#
# #asserting that the browser title is correct
# assert browser.title == "Your Account Has Been Created!"

#closing the browser
browser.quit()
