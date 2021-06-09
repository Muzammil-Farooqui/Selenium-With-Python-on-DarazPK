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
#Global Variable

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Get URL
def getURL(url):
    driver.get(url)
    time.sleep(1)
    try:
        driver.find_element_by_xpath("/html/body/div[7]//div/div/div[3]/button[1]").click()
    except:
        print("Didn't find not interested button")
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Close Browser
def closeBrowser():
    time.sleep(3)
    driver.close()
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Scroll Down Page
def scrollDownPage(SectionTitleXpath):
    SectionTitle = driver.find_element_by_xpath(SectionTitleXpath)
    driver.execute_script("arguments[0].scrollIntoView();", SectionTitle)
    time.sleep(2)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
def slideForvarification(xpath, x, y):
    Source = driver.find_element_by_id(xpath)
    # Target = driver.find_element_by_xpath("//div[@id='box106']")
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(Source, x, y).perform()
    time.sleep(3)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#Exploring Website Function
def exploreSite():
    scrollDownPage("/html/body/div[4]/div[6]/div[1]/h3")   #scroll down page to Daraz Mall Section
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div[8]/div[2]/div[1]/div/div[1]/div[4]/a/div').click()          #Click on luner ferniture product
    time.sleep(1)
    try:
        driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/span").click()                               #close the pop if displayed
    except:
        print("No alert to close")
    scrollDownPage("/html/body/div[4]/div/div[8]/div[1]/div[1]/div/h2")                                             #scroll page Product details list
    scrollDownPage("/html/body/div[4]/div/div[8]/div[1]/div[2]/div/div/div[1]/div[1]/h2")                           # scroll page footer
    driver.find_element_by_xpath("/html/body/div[5]/div/section/div[1]/div/div[1]/ul[2]/li[2]/a").click()
    scrollDownPage("/html/body/div[2]/div[7]/div")                                                                  # scroll page to testimonials
    scrollDownPage("/html/body/div[2]/div[5]/div/div/ul/li/a/img")                                                  # Scroll page upto step 2
    driver.find_element_by_xpath("/html/body/div[2]/div[5]/div/div/ul/li/a/img").click()                            #click on step 2
    time.sleep(3)
    # getURL("https://sellercenter.daraz.pk/apps/register/registration?bizType=0")
    # time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/div/article/div[2]/div[1]/div/div/div/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div[1]/button").click()   # click on local seller card
    time.sleep(3)

    radio_btn = driver.find_element_by_xpath("/html/body/div[1]/div/article/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/label[2]/span[1]/input")
    if(radio_btn.is_selected() == True):
        pass
    else:
        radio_btn.click()

    # driver.find_element_by_xpath("/html/body/div[1]/div/article/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/label[2]/span[1]/input").click()  # select Business radio button
    driver.find_element_by_xpath("/html/body/div[1]/div/article/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[11]/div[1]/span/span[2]/input").send_keys("3459556489")
    driver.find_element_by_xpath("/html/body/div[1]/div/article/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[12]/span").click()
    time.sleep(3)
    slideForvarification("nc_2_n1z", 410, 0)     # Slide for varification code
    driver.find_element_by_xpath("/html/body/div[1]/div/article/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[13]/div/span/input").send_keys("123456")        # input varification code
    driver.find_element_by_xpath("/html/body/div[1]/div/article/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[14]/div[1]/span/input").send_keys("Muhammad@0987")   #input password
    driver.find_element_by_xpath("/html/body/div[1]/div/article/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[15]/div/span/input"). send_keys("Muhammad@0987")
    driver.find_element_by_xpath("/html/body/div[1]/div/article/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[16]/div/span/input").send_keys("muhammad@gmail.com")
    driver.find_element_by_xpath("/html/body/div[1]/div/article/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[17]/div/span/input").send_keys("Asan Buy")
    driver.find_element_by_link_text("I have a referral code").click()
    driver.find_element_by_xpath("/html/body/div[1]/div/article/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[19]/div/span/input").send_keys("456464")
    driver.find_element_by_xpath("/html/body/div[1]/div/article/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[20]/div/label/span[1]/input").click()

    # driver.execute_script("window.scrollBy(0,1000)","")
    # time.sleep(1)
    # driver.execute_script("window.scrollBy(1000,2000)","")
    # time.sleep(1)
    # # driver.execute_script("window.scrollBy(0,2000)", "")
    # # time.sleep(1)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
def moveBack():
    driver.back()
    time.sleep(1)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------- Main --------------------------------------------------------------------------------------
if __name__=="__main__":
    getURL("https://www.daraz.pk/")    # enter Dara url to explore website
    exploreSite()                      # call explore website function
    closeBrowser()                     # call close browser function