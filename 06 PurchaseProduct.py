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
    time.sleep(1)

#Close Browser
def closeBrowser():
    time.sleep(3)
    driver.close()

def scrollDownPage(SectionTitleXpath):
    SectioTitle = driver.find_element_by_xpath(SectionTitleXpath)
    driver.execute_script("arguments[0].scrollIntoView();", SectioTitle)
    time.sleep(2)

def switchFrame(FrameName):
    driver.switch_to.frame(FrameName)

def login(email, password):
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[2]/form/div/div[1]/div[1]/input").send_keys(email)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[2]/form/div/div[1]/div[2]/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[1]/button").click()

def productImagesView(xpath):
    try:
        driver.find_element_by_xpath(xpath).click()
    except:
        print("not found")

    time.sleep(1)

#Increase Number of quantity Function
def increaseQuantity(qty):
    for i in range(0, qty):
        driver.find_element_by_xpath('//*[@id="module_quantity-input"]/div/div/div/div[1]/a[1]/span').click()

    time.sleep(1)

#Decrease Number of quantity Function
def decreaseQuantity(qty):
    for i in range(0, qty):
        try:
            driver.find_element_by_xpath('//*[@id="module_quantity-input"]/div/div/div/div[1]/a[2]/span').click()
        except:
            print("Quantity is 0")
    time.sleep(1)

#purchase prduct function
def purchaseProduct(ProductXpath, email, password):
    driver.find_element_by_xpath(ProductXpath).click()                  #click on product
    time.sleep(1)

    try:
        driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/span").click()   #close the pop if displayed
    except:
        print("No alert to close")

    #call product image Function
    productImagesView("/html/body/div[4]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[2]/div")    #click on first image
    productImagesView("/html/body/div[4]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div")    #click on first image
    productImagesView("/html/body/div[4]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[4]/div")    #click on first image

    #call quantity functions
    increaseQuantity(4)   #increase quantity to 5
    decreaseQuantity(6)   #decrease quantity to 1

    driver.find_element_by_xpath('//*[@id="module_add_to_cart"]/div/button[1]').click()                  #click on on buy product button
    time.sleep(3)

    driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)                                       #close login frame

if __name__=="__main__":
    getURL("https://www.daraz.pk/")
    scrollDownPage('//*[@id="hp-just-for-you"]/div[1]/h3')
    purchaseProduct("/html/body/div[4]/div[8]/div[2]/div[1]/div/div[1]/div[1]/a/div", "test@gmail.com", "123456789")
    # login("test@gmail.com", "123456789")
    closeBrowser()