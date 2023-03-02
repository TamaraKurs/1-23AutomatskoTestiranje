import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()

#navigacija na stranicu
navigationPage = driver.get("https://www.google.com")

#unos u polje
inputField = driver.find_element("id", "input").send_keys("SmartInIt")

