'''
Files a citizen complaint on the ldeq website with Cindy's info
'''

import random
import pdb
from selenium.webdriver.common.by import By
from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless
import time
import random
import json
from pathlib import Path
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


COMPLAINT_FORM_URL = "https://internet.deq.louisiana.gov/portal/ONLINESERVICES/FORMS/FILE-A-CITIZEN-COMPLAINT"
OPTIONAL = True
SOLVERKEY = "2ee4b597258f59049433249fa6e9a4cf"

'''
HELPER METHODS
'''

def enterInput(browser, id, value, optional = False):
    if optional and not value: return
    input_element = browser.find_element(By.ID, id)
    input_element.send_keys(value)
    browser.implicitly_wait(random.randint(1,10))

def selectDropdown(browser, id, value, optional = False):
    if optional and not value: return
    dropdown_element = Select(browser.find_element(By.ID, id))
    dropdown_element.select_by_value(value)
    browser.implicitly_wait(random.randint(1,10))

def find_between(s, start, end):
    return (s.split(start))[1].split(end)[0]

# It's usefull to save cookies so chances of having to spend anticaptcha API are lower
def save_cookies(driver, path="cookies.json"):
    with open(path, 'w') as filehandler:
        json.dump(driver.get_cookies(), filehandler)
    print("[ ] Session cookies successfully saved.")
    return

def load_cookies(driver, path="cookies.json"):
    driver.get(COMPLAINT_FORM_URL)
    my_file = Path(path)
    if my_file.is_file():
        with open(path, 'r') as cookiesfile:
            cookies = json.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)
        print("[ ] Session cookies successfully Loaded.")
        return
    else:
        print("[ ] Session cookies file does not exists.")
        return

def solve_recaptcha(driver):
    while True:
        try:
            if driver.find_element(By.CLASS_NAME, "g-recaptcha"): # Try to find if theres recaptcha on the page
                print("[ ] reCAPTCHA detected")
            else:
                print("[ ] reCAPTCHA not detected")
                return # If it doesn't, just returns
            print("[ ] Starting anticaptcha")
            WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']"))) # Wait for recaptcha iframe to be available and.. Time out 10 secs
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']")) )# Wait for recaptcha anchor to be clickable. Time out 10 secs
            driver.switch_to.default_content()
            data_sitekey = driver.find_element(By.CLASS_NAME, 'g-recaptcha').get_attribute('data-sitekey') # The sitekey will be needed for anticaptcha to do the job
            solver = recaptchaV2Proxyless() # Here the magic starts
            solver.set_verbose(0)
            solver.set_key(SOLVERKEY)
            solver.set_website_url(COMPLAINT_FORM_URL)
            solver.set_website_key(data_sitekey)
            g_response = solver.solve_and_return_solution()
            if g_response != 0: # If answer not 0, success!
                print("[ ] g-response SUCCESS")
                driver.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "{}";'.format(g_response)) # Sends captcha solution
                return
            else:
                print("[ ] Task finished with error "+solver.error_code)
                print("[ ] Reporting anticaptcha error via API.")
                solver.report_incorrect_image_captcha() # Report anticaptcha error to the API
                print("[ ] Refreshing page...")
                driver.refresh() # Refresh page and try again if anticaptcha didn't work
                print("[ ] Trying again.")
        except Exception as err:
            print(err)
            driver.close()
            exit()

def submit_form(browser):
    browser.find_element(By.XPATH, '//*[@id="lxT513"]/table[3]/tbody/tr/td[2]/a').click()
    return

def fill_out_form(browser, submitter_data, site_data):
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
    enterInput(browser, "txtincidentzip", site_data["zipcode"], OPTIONAL)
    enterInput(browser, "txtdateofdis", site_data["date"])
    enterInput(browser, "txtnoticedtimebegan", site_data["start_time"])
    enterInput(browser, "txtnoticedtimeended", site_data["end_time"])
    selectDropdown(browser, "ddincidentparish", site_data["parish"])
    selectDropdown(browser, "ddincidentmediaaffected", site_data["media_affected"], OPTIONAL)
    enterInput(browser, "txtdescriptionofcomplaint", site_data["description"])
    enterInput(browser, "txtdirectionsforreachingthesite", site_data["directions_to_site"], OPTIONAL)

def complain(submitter_data, site_data):
    options = Options()
    options.browserName = "Chrome"
    options.browserVersion = "103.0"
    browser = webdriver.Chrome(options=options)

    while True:
        try:
            load_cookies(browser) # Fistly try to load cookies previously saved
            browser.get(COMPLAINT_FORM_URL) # Calls for target url
            solve_recaptcha(browser) # Call function to handle captcha
            print("[ ] Sleeping, pretending to be a human")
            time.sleep(random.uniform(4.0, 7.0)) # Usefull line to pretend being a human
            save_cookies(browser) # Save cookies for eventual later use
            print("[ ] Filling out form")
            fill_out_form(browser, submitter_data, site_data)
            print("[ ] Submiting form")
            submit_form(browser)
            # if "Verification Success" in browser.find_element(By.XPATH, '/html/body/div').text: # Check if next page is what we expect
            #     print("[ ] Verification Success... Hooray!")
            print("[ ] Finished submission. Closing browser")
            browser.close()
            return
        except Exception as err:
            print(err)
            browser.close()
            exit()

def formatDate(timestamp):
    # e.g. "06/12/2023"
    d = datetime.fromtimestamp(timestamp)
    return d.strftime('%m/%d/%Y')

def formatTime(timestamp):
    # e.g. "11:30:00"
    d = datetime.fromtimestamp(timestamp)
    return d.strftime('%H:%M:%S')
