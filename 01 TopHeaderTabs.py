import unittest
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C://Automation Drivers//Selenium Web Drivers//chromedriver_win32//chromedriver.exe")
driver.maximize_window()

#Get URL
def getURL(url):
    driver.get(url)
    time.sleep(2)

#Close Browser
def closeBrowser():
    time.sleep(3)
    driver.close()

#Switching to Alert
# driver.switch_to.alert.dismiss()


if __name__=="__main__":
    getURL("https://www.daraz.pk/")              #Hit Url
    driver.find_element_by_link_text('//*[@id="topActionSell"]/a').click()
    closeBrowser()





