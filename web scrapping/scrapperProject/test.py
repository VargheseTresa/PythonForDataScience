# web scrapper implementation using selenium
import time
from selenium import webdriver
from bs4 import BeautifulSoup

searchString = 'samsung'
DRIVER_PATH    = "C:\\Datasets\\chromedriver"
URL = "https://www.flipkart.com/search?q=" + searchString

try:
    browser = webdriver.Chrome(DRIVER_PATH)
    browser.get(URL)

    # Give the browser time to load all content.
    time.sleep(3)


    links = browser.find_elements_by_css_selector("._2kHMtA")

    phone1 = links[0]
    phone1.click()
    time.sleep(3)

    content = browser.find_elements_by_css_selector(".col _2wzgFH")

    print(content)

except Exception as e:
    print(e)
'''

    start = content[0].get_attribute('innerHTML')
    # Beautiful soup allows us to remove HTML tags from our content if it exists.
    soup = BeautifulSoup(start, features="html.parser")
    print(soup.get_text())
'''


