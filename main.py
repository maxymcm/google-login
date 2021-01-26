from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import getpass

password = getpass.getpass("Password: ")

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)

driver.get("https://www.google.com")

driver.find_element_by_xpath("//a[@id='gb_70']").click()
time.sleep(1)
emailField = driver.find_element_by_xpath("//input[@type='email']")
emailField.send_keys("maxtantutorial@gmail.com")

driver.find_element_by_xpath("//div[@id='identifierNext']").click()

time.sleep(1)
passwordField = driver.find_element_by_xpath("//input[@type='password']")
passwordField.send_keys(password)

driver.find_element_by_xpath("//div[@id='passwordNext']").click()

#ATTEMPTS TO PRESS CONFIRM BUTTON
#IF IT DOESN'T EXIST, IT WON'T PRESS IT
try:
    time.sleep(2)
    buttons = driver.find_elements_by_xpath("//div[@role='button']")
    buttons[1].click()
except:
    pass
