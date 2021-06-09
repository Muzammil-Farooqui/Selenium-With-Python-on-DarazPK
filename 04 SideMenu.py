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

#Get URL Function
def getURL(url):
    driver.get(url)

#Close Browser Function
def closeBrowser():
    time.sleep(3)
    driver.close()

#select category Function
def categorySelection():
    FirstList = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/ul/li[3]/a/span")                    #Mouse hover on first list
    SecondList = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/ul/ul[3]/li[6]/a/span")             #Mouse hover on Second list
    ThirdList = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div/ul/ul[3]/li[6]/ul/li[2]/a/span")     #Mouse hover on third list

    actions = ActionChains(driver)                                                                                                              #call action chain function
    actions.move_to_element(FirstList).move_to_element(SecondList).move_to_element(ThirdList).click().perform()                                 #Perform hover action


#Switching to Alert
# driver.switch_to.alert.dismiss()

#Main
if __name__=="__main__":
    getURL("https://www.daraz.pk/")
    categorySelection()
    closeBrowser()