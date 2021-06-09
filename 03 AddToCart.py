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

#Login Function
def login(email, password):
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[1]/input").send_keys(email)           #Enter Email
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[2]/input").send_keys(password)        #Enter Password
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[2]/div[1]/button").click()                   #click on login button

#Add to cart Function
def addToCart(email, password):
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div/div[2]/div/div[3]/a/span[1]").click()                    #click on add to cart icon on header
    time.sleep(1)                                                                                                                   #wait for one second
    login(email,password)                                                                                                           #call login function

#Main
if __name__=="__main__":
    getURL("https://www.daraz.pk/")                 #call Get URL Function
    addToCart("test@gmail.com", "123456879")        #call add to cart function
    closeBrowser()                                  #call close browser function