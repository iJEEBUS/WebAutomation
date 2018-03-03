"""
Author: Ronald Rounsifer
Date: 11/08/2017
Version: 1.0
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


site = 'https://www.bing.com'

driver = webdriver.Firefox()

driver.get(site)

usernameInput = driver.find_element_by_name('session[username_or_email]')
passwordInput = driver.find_element_by_name('session[password]')