"""
Author: Ronald Rounsifer
Date: 11/08/2017
Version: 1.0
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def  createDriver():
	return webdriver.Chrome()

def getSite(driver, site):
	return driver.get(site)

def getLoginInputs(driver):
	return driver.find_element_by_name("user"), driver.find_element_by_name("passwd")

def login(usernameInput, passwordInput, site, username, password):
	print 'Logging into %s as %s' % (site, username)
	usernameInput.send_keys(username)
	passwordInput.send_keys(password)
	passwordInput.send_keys(Keys.RETURN)

def clickTitle(driver, title):
	post = driver.find_element_by_link_text(title)
	return webdriver.ActionChains(driver).click(post).perform()

def changeWindow(driver, num):
	driver.switch_to_window(driver.window_handles[num])
	return

def closeWindow(driver):
	driver.close()
	return

site = "https://www.reddit.com/"
name = raw_input('Username: ')
pwd = raw_input("Password: ")
title = "The plural of \"Octopus\""


# Create the driver object
driver = createDriver()

# Load the site using the driver
getSite(driver, site)

# Find username and password login inputs
usernameInput, passwordInput = getLoginInputs(driver)

# Login to the site
login(usernameInput, passwordInput, site, name, pwd)

time.sleep(3)

# Click on the title of a post
clickTitle(driver, title)

exit = raw_input('Close? y/n\n')

if str.lower(exit) in ['yes', 'y', 'ye']:
	# Change the active window
	changeWindow(driver, 1)
	
	# Close the window
	closeWindow(driver)

	changeWindow(driver, 0)

	driver.quit()