import time

from selenium import webdriver
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome = webdriver.Chrome()
try:
    chrome.get('http://192.168.99.100:5000/')
    print(chrome.title)
# except:
    # chrome.quit()

