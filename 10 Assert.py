import unittest
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AppTesting(unittest.TestCase):

    def test_assrt(self):
        self.driver = webdriver.Chrome(executable_path="C://Automation Drivers//Selenium Web Drivers//chromedriver_win32//chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://member.daraz.pk/user/login?spm=a2a0e.login_signup.header.d5.6f327d68C4cpdV&redirect=https%3A%2F%2Fmember.daraz.pk%2Fuser%2Flogin%3Fspm%3Da2a0e.login_signup.header.d5.36737d687XiF8R%26redirect%3Dhttps%253A%252F%252Fmember.daraz.pk%252Fuser%252Flogin%253Fspm%253Da2a0e.home.header.d5.91454937XYBcfY%2526redirect%253Dhttps%25253A%25252F%25252Fwww.daraz.pk%25252F%25253Fspm%25253Da2a0e.searchlist.header.dhome.2d6577bamBiqMa%252523")
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[1]/input").send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[1]/input").click()
        emailvalidation = "You can't leave this empty"
        self.assertTrue(emailvalidation == "You can't leave this empty.", "Empty field validation")

if __name__ == "__main__":
    unittest.main()
