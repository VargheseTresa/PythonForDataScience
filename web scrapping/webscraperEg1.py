import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


DRIVER_PATH    = "C:\\Datasets\\chromedriver"
URL = "https://www.rottentomatoes.com/critics/latest_reviews"
browser = None

# This loads webdriver from the local machine if it exists.
try:
    browser = webdriver.Chrome(DRIVER_PATH)

# If a webdriver not found error occurs it is then downloaded.
except:
    print("webdriver not found. Update 'DRIVER_PATH' with file path in the download.")
    browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get(URL)

# Give the browser time to load all content.
time.sleep(3)

content = browser.find_elements_by_css_selector(".critics-latest-reviews__data-review .a")
print(type(content[0]))
# content is a list of elements of type selenium.webdriver.remote.webelement.WebElement
for e in content:
    start = e.get_attribute('innerHTML')
    # Beautiful soup allows us to remove HTML tags from our content if it exists.
    soup = BeautifulSoup(start, features="lxml")
    print(soup.get_text())
    print("***")  # Go to new line.


