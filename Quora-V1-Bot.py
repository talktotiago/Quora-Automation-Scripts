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

driver = webdriver.Chrome()
driver.get("https://pt.quora.com/")
time.sleep(2)

#Important WebElements found by Selenium
linktoquestion = driver.find_elements_by_class_name('a2a_section') 
modalwindow = driver.find_element_by_id('react_loadable')


StartAtQuestion = 35 #Change to 0 to click from the first question to last


def LoginPage():
    #Credentials
    username = 'tiagoluizd@gmail.com'
    pwd = 'Amoroma1982'
    #Login Form
    form = driver.find_element_by_class_name("form_inputs")
    usernamefield = form.find_element_by_name("email")
    usernamefield.send_keys(username)
    pwdfield = form.find_element_by_name("password")
    pwdfield.send_keys(pwd)
    pwdfield.send_keys(Keys.RETURN)
#LoginPage() - Self Explanatory
def Partners():
    time.sleep(2)
    profile_img=driver.find_element_by_class_name('u-height--100').click()
    time.sleep(1)
    content_menu = driver.find_element_by_class_name('hover_menu_contents')
    partnerslink = driver.find_element_by_link_text('Parceiros')
    partnerslink.click()
#Partners() = Partners Section
def RollDown():
    page = driver.find_element_by_tag_name('body')
    for i in range (0,10):
        time.sleep(0.5)
        page.send_keys(Keys.END)
        time.sleep(0.5)
    page.send_keys(Keys.HOME)
#Scroll to bottom and up - set to iterate 10 times. If you have too many questions, add a number higher than 10

#Define Click Question and Ask To Answer
def Ask2Answer():
    time.sleep(2)#Closer to 1 - faster but with chances to crash. Closer to 4. Safer but slower. 
    modalwindow = driver.find_element_by_id('react_loadable')
    try:
        for i in range (2,27,1):
            invitebnclick = modalwindow.find_element_by_xpath('//*[@id="react_loadable"]/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/div/div['+repr(i)+']/div/div/div[3]/div')
            invitebnclick.click()
            time.sleep(1)
    except NoSuchElementException as exception:
        time.sleep(1)
        finish_btn = modalwindow.find_element_by_xpath('//*[@id="react_loadable"]/div/div[1]/div/div/div/div/div[2]/div/div/div[3]/div[2]/span')
        finish_btn.click()        
    else:
        time.sleep(1)
        closequestion.click()
        


def OpenQuestions():
    linktoquestion = driver.find_elements_by_class_name('a2a_section')
    print("Total of Questions Found "+ repr(len(linktoquestion)))
    for i in range (StartAtQuestion,((len(linktoquestion))+1),1):  #Change the first argument to jump to a different question in the list and continue from there
        time.sleep(1)
        print("Opening "+repr([i])+" of "+repr(len(linktoquestion)))
        linktoquestion[i].click()
        time.sleep(2)
        Ask2Answer()
LoginPage()
Partners()
RollDown()
OpenQuestions()



