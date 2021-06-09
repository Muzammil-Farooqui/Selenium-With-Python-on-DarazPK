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
driver.maximize_window()     #Maximze window

#Get URL Function
def getURL(url):
    driver.get(url)

#Close Browser Function
def closeBrowser():
    time.sleep(3)
    driver.close()
#Search Product Function
def Search(txt):
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/form/div/div[1]/input[1]").send_keys(txt)           #Type product Name
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/form/div/div[1]/input[1]").send_keys(Keys.ENTER)    #Press Enter to search


if __name__=="__main__":
    getURL("https://www.daraz.pk/")         #Hit URL
    Search("Iphone")                        #call Product search function
    closeBrowser()                          #call close browser function