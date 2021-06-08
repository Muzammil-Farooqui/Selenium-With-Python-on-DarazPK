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

#Global Variable

ScrollDownValue = 2000


#Get URL
def getURL(url):
    driver.get(url)

#Close Browser
def closeBrowser():
    time.sleep(3)
    driver.close()


# def scrollDownPage(xpath):
#     scrollDown = driver.find_element_by_xpath(xpath)
#     driver.execute_script("arguments[0].scrollIntoView();", scrollDown)

def scrollDownPage(ScrollDownValue):
    driver.execute_script("window.scrollBy(0,ScrollDownValue)", "")
    ScrollDownValue = ScrollDownValue+2000

def exploreProduct(ProductXpath):
    driver.find_element_by_xpath(ProductXpath).click()
    time.sleep(1)

def moveBack():
    driver.back()
    time.sleep(1)

if __name__=="__main__":
    getURL("https://www.daraz.pk/")

    productList = ["/html/body/div[4]/div[3]/div[2]/div[2]/a[4]", "/html/body/div[4]/div[5]/div[2]/section/div/a[4]/div[2]/img" ]
    ScrollDownValue = 2000
    for product in productList:
        scrollDownPage()
        exploreProduct(product)
        moveBack()


    closeBrowser()