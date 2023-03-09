from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

#navigacija na stranicu
navigationPage = driver.get("https://elearn.smartinit.net/login/index.php")

#povecati prozor
driver.maximize_window()

#implicitno cekanje
driver.implicitly_wait(10)

#logovati se na stranicu
userName = driver.find_element("id", "username").send_keys("tamara.mitrovic")
password = driver.find_element("id","password").send_keys("123")
logInButton = driver.find_element("id","loginbtn").click()

#eksplicitno cekanje
WebDriverWait(driver,10).until(
    EC.presence_of_element_located(("id","essentialicons")))

#validacija stranice na koju smo navigirani
homePage = driver.find_element("xpath", "//h2[contains(text(), 'Moji kursevi')]").get_attribute("innerText")
assert homePage == "Moji kursevi"

driver.quit()

print("Test passed")