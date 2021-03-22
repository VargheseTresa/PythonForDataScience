import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re


DRIVER_PATH    = "C:\\Datasets\\chromedriver"
URL = "https://vpl.bibliocommons.com/events/search/index"

browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

# Give the browser time to load all content.
time.sleep(3)

# To click show more button and load more content before scrapping
button = browser.find_element_by_css_selector(".btn-lg")
for i in range(0,10):
    button.click()
    '''
    If you see the following error increase the sleep time:
    ElementClickInterceptedException: element click intercepted:
    '''
    print("Count: ", str(i))
    time.sleep(3)
print("done loop")


content = browser.find_elements_by_css_selector(".event-row")
for e in content:
    textContent = e.get_attribute('innerHTML')
    # Beautiful soup removes HTML tags from our content if it exists.
    soup = BeautifulSoup(textContent, features="lxml")
    rawString = soup.get_text().strip()

    # Remove hidden characters for tabs and new lines.
    rawString = re.sub(r"[\n\t]*", "", rawString)

    # Replace two or more consecutive empty spaces with '*'
    rawString = re.sub('[ ]{2,}', '*', rawString)

    # Fine tune the results so they can be parsed.
    rawString = rawString.replace("Location", "Location*")
    rawString = rawString.replace("Registration closed", "Registration closed*")
    rawString = rawString.replace("Registration required", "Registration required*")
    rawString = rawString.replace("In Progress", "*In Progress*")
    rawString = rawString.replace("*/*", "/")
    rawString = rawString.replace("Full*", "*Full*")

    eventArray = rawString.split('*')

    EVENT_NAME = 0
    EVENT_DATE = 1
    EVENT_TIME = 2
    eventName = eventArray[EVENT_NAME]
    eventDate = eventArray[EVENT_DATE].strip()  # remove leading and trailing spaces
    eventTime = eventArray[EVENT_TIME].strip()  # remove leading and trailing spaces
    location = eventArray[len(eventArray) - 1]
    print("Name:     " + eventName)
    print("Date:     " + eventDate)
    print("Time:     " + eventTime)
    print("Location: " + location)
    print("***")


