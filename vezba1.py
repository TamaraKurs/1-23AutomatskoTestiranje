from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest

class TestBalanceCheck(unittest.TestCase):

    def test(self):
        driver = webdriver.Chrome()

        #navigacija na stranicu
        navigateToPage = driver.get("https://www.nationalgeographic.com/")

        #verifikacija stranice
        verification = driver.find_element(By.CLASS_NAME, "GeneralHeading__Header")

        self.assertEqual("Tutorialspoint", "Tutorialspoint")
    
t = TestBalanceCheck()
t.test()

