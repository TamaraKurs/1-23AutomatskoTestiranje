from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

#navigacija na stranicu
navigateToPage = driver.get("https://www.nationalgeographic.com/")

#pronalazenje elementa i klik na isti
elementStranice = driver.find_element("id", "b7c38d77-1fdf-4e28-801f-1da62484143b").click()


