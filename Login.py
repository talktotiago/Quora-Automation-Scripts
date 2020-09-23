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
#Login to Quora
def LoginPage():
    #Credentials
    username = 'enter username here'
    pwd = 'enter password here'
    #Login Form
    form = driver.find_element_by_class_name("form_inputs")
    usernamefield = form.find_element_by_name("email")
    usernamefield.send_keys(username)
    pwdfield = form.find_element_by_name("password")
    pwdfield.send_keys(pwd)
    pwdfield.send_keys(Keys.RETURN)
LoginPage()
