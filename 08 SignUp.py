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

#-------------------------------------------------------------------------------------------------------------------------------------------------------
driver=webdriver.Chrome(executable_path="C://Automation Drivers//Selenium Web Drivers//chromedriver_win32//chromedriver.exe")
driver.maximize_window()
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Get URL
def getURL(url):
    driver.get(url)
    time.sleep(1)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Close Browser
def closeBrowser():
    time.sleep(3)
    driver.close()
#-------------------------------------------------------------------------------------------------------------------------------------------------------
def signUp():
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]/div[1]/div/div[7]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[1]/input").send_keys("03333333333")

    slideForCode("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[2]/div/div/div/div/div[1]/span")

    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[2]/div[1]/input").send_keys("123456")
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[3]/input").send_keys("qwerty1")
    # driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[3]/div[1]").click()
    # selectDropDownByXpath("/html/body/div[7]/div/div", "August")
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[1]/span/span").click()
    # driver.find_element_by_xpath("/html/body/div[7]/div/div/ul/li[10]").click()
    time.sleep(2)

    # selectDropDownByXpath("/html/body/div[7]/div/div/ul/li[3]", "August")
#-------------------------------------------------------------------------------------------------------------------------------------------------------
def slideForCode(xpath):
    Source = driver.find_element_by_xpath(xpath)
    # Target = driver.find_element_by_xpath("//div[@id='box106']")
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(Source, 340, 0).perform()
    time.sleep(3)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
def selectDropDownByXpath(xpath, text):
    Select(driver.find_element_by_name(xpath)).select_by_visible_text(text)
    time.sleep(1)


#----------------------------------------------------------------- Main ---------------------------------------------------------------------------------
if __name__=="__main__":
    getURL("https://www.daraz.pk/")
    # getURL("https://member.daraz.pk/user/register?spm=a2a0e.home.header.d6.35e349379e8vpr")
    driver.find_element_by_xpath('//*[@id="anonSignup"]/a').click()                                 # Click on signup button
    signUp()                                                                                        # Call signup Function
    closeBrowser()