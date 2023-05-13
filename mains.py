# Ignore this , This code is not part of SAMARTH but rather a test code !!

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service

service = Service('/opt/homebrew/bin/chromedriver')
driver = webdriver.Chrome(service=service)
# specify the path to the chromedriver executable
# driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver')

# open the ChatGPT website
driver.get('https://www.chatgpt.com')

# find the login button and click on it
login_button = driver.find_element_by_xpath('//button[contains(text(),"Log In")]')
login_button.click()

# enter the username and password
username_input = driver.find_element_by_xpath('//input[@name="username"]')
username_input.send_keys('XYZ')
password_input = driver.find_element_by_xpath('//input[@name="password"]')
password_input.send_keys('Y')

# submit the login form
submit_button = driver.find_element_by_xpath('//button[@type="submit"]')
submit_button.click()

# wait for the page to load
time.sleep(5)

# find the search bar and enter the search query
search_bar = driver.find_element_by_xpath('//input[@name="search"]')
search_bar.send_keys('asd')
search_bar.send_keys(Keys.RETURN)

# close the browser
driver.quit()
