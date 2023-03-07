from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

#navigacija na stranicu
navigationPage = driver.get("https://elearn.smartinit.net/login/index.php")

#unos u polje
inputField = driver.find_element("id", "username").send_keys("tamara.mitrovic")
passwordField = driver.find_element("id","password").send_keys("")
logInButton = driver.find_element("id","loginbtn").click()