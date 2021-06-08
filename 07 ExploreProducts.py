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
    time.sleep(1)
    try:
        driver.find_element_by_xpath("/html/body/div[7]//div/div/div[3]/button[1]").click()
    except:
        print("Didn't find not interested button")

#Close Browser
def closeBrowser():
    time.sleep(3)
    driver.close()


# def scrollDownPage(xpath):
#     scrollDown = driver.find_element_by_xpath(xpath)
#     driver.execute_script("arguments[0].scrollIntoView();", scrollDown)

def scrollDownPage(SectionTitleXpath):
    SectioTitle = driver.find_element_by_xpath(SectionTitleXpath)
    driver.execute_script("arguments[0].scrollIntoView();", SectioTitle)


def exploreProduct(ProductXpath):
    driver.find_element_by_xpath(ProductXpath).click()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,1000)","")
    time.sleep(1)
    driver.execute_script("window.scrollBy(1000,2000)","")
    time.sleep(1)
    # driver.execute_script("window.scrollBy(0,2000)", "")
    # time.sleep(1)

def moveBack():
    driver.back()
    time.sleep(1)

if __name__=="__main__":
    getURL("https://www.daraz.pk/")

    ScrollDownXpathList = ["/html/body/div[4]/div[4]/div[1]/h3", "/html/body/div[4]/div[5]/div[1]/h3", "/html/body/div[4]/div[6]/div[1]/h3", "/html/body/div[4]/div[7]/div[1]/h3"]
    productList = ["/html/body/div[4]/div[3]/div[2]/div[2]/a[4]", "/html/body/div[4]/div[5]/div[2]/section/div/a[4]/div[2]/img","/html/body/div[4]/div[6]/div[2]/div/div[6]/a/div[2]/span", "/html/body/div[4]/div[7]/div[2]/div[1]/div/div[1]/div[1]/a/div/div[2]/div[2]/span"]

    i = 0
    for product in productList:
        scrollDownPage(ScrollDownXpathList[i])
        i = i + 1
        # driver.execute_script("window.scrollBy(0,2000)", "")
        time.sleep(1)
        exploreProduct(product)
        moveBack()

    closeBrowser()