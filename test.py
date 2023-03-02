import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

#navigacija na stranicu
navigationPage = driver.get("https://www.google.com")

#unos u polje
inputField = driver.find_element("xpath", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("SmartInIt")
