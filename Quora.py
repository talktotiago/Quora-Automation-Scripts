#Import Selenium Dependencies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import chromedriver_binary  # Adds chromedriver binary to path
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

startquestion = 24

driver = webdriver.Chrome()
driver.get("https://pt.quora.com/")
time.sleep(2)


def LoginPage():
    #Credentials
    username = 'username here'
    pwd = 'password here'
    #Login Form
    form = driver.find_element_by_class_name("form_inputs")
    usernamefield = form.find_element_by_name("email")
    usernamefield.send_keys(username)
    pwdfield = form.find_element_by_name("password")
    pwdfield.send_keys(pwd)
    pwdfield.send_keys(Keys.RETURN)
LoginPage()
def Partners():
    time.sleep(2)
    profile_img=driver.find_element_by_class_name('u-height--100').click()
    time.sleep(1)
    content_menu = driver.find_element_by_class_name('hover_menu_contents')
    partnerslink = driver.find_element_by_link_text('Parceiros')
    partnerslink.click()
Partners()
def RollDown():
    page = driver.find_element_by_tag_name('body')
    for i in range (0,10):
        time.sleep(0.5)
        page.send_keys(Keys.END)
        time.sleep(0.5)
    page.send_keys(Keys.HOME)
RollDown()


#Define Click Question and Ask To Answer
linktoquestion = driver.find_elements_by_class_name('a2a_section')
modalwindow = driver.find_element_by_id('react_loadable')
contentmodalwindow = modalwindow.find_element_by_class_name('q-box')
approachsvg = contentmodalwindow.find_elements_by_tag_name('svg')

def Ask2Answer():
    time.sleep(3)
    try:
        for i in range (2,29,1):
            invitebnclick = modalwindow.find_element_by_xpath('//*[@id="react_loadable"]/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/div/div['+repr(i)+']/div/div/div[3]/div')
            invitebnclick.click()
            time.sleep(0.3)
    except NoSuchElementException as exception:
        closequestion=modalwindow.find_element_by_xpath('//*[@id="react_loadable"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div')
        closequestion.click()


def OpenQuestions():
    print("there's a total of "+ repr(len(linktoquestion))+" you have made")
    for i in range (startquestion,len(linktoquestion),1):
        linktoquestion[i].click()
        time.sleep(1)
        print("Opening ["+startquestion+"] of "+repr(len(linktoquestion))+" questions")        
    Ask2Answer()
OpenQuestions()



