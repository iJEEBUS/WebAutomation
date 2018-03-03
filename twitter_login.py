"""
Author: Ronald Rounsifer
Date: 11/08/2017
Version: 1.0
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time

username = 'banksybottwitter@gmail.com' #raw_input('Username: ')
password =  'hamilton'#getpass.getpass()
site = 'https://twitter.com'

driver = webdriver.Chrome()

driver.get(site)

usernameInput = driver.find_element_by_name('session[username_or_email]')
passwordInput = driver.find_element_by_name('session[password]')

usernameInput.send_keys(username)
passwordInput.send_keys(password)
passwordInput.send_keys(Keys.RETURN)