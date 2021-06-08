import unittest
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver=webdriver.Chrome(executable_path="C://Automation Drivers//Selenium Web Drivers//chromedriver_win32//chromedriver.exe")
driver.maximize_window()

#Get URL
def getURL(url):
    driver.get(url)

#Close Browser
def closeBrowser():
    time.sleep(3)
    driver.close()

def botomMenuTab(TabXpath):
    driver.find_element_by_xpath(TabXpath).click()


if __name__=="__main__":
    getURL("https://www.daraz.pk/")
    botomMenuTab("/html/body/div[4]/div[2]/div/div[2]/a")
    closeBrowser()