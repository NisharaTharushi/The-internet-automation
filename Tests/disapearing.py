from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  

driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)


# find Disapearing link
link = driver.find_element(By.LINK_TEXT, "Disappearing Elements")
print("Disappearing link found")
link.click()

time.sleep(2)

# ckeck the h3 name Disappearing Elements 
h3 = driver.find_element(By.TAG_NAME, "h3")
print("h3 name is: " + h3.text)

time.sleep(2)

# Home button find by href
home = driver.find_element(By.LINK_TEXT, "Home")
print("Home button found")
home.click()

driver.back()
time.sleep(2)


# About button find by href
about = driver.find_element(By.LINK_TEXT, "About")
print("About button found")
about.click()

driver.back()
time.sleep(2)


# Contact Us button find by href
contact = driver.find_element(By.LINK_TEXT, "Contact Us")
print("Contact Us button found")
contact.click()

driver.back()
time.sleep(2)


# Portfolio button find by href
portfolio = driver.find_element(By.LINK_TEXT, "Portfolio")
print("Portfolio button found")
portfolio.click()

driver.back()
time.sleep(2)


# Elemental Selenium link find by href
elemental = driver.find_element(By.LINK_TEXT, "Elemental Selenium")
print("Elemental Selenium link found")
elemental.click()

driver.back()
time.sleep(2)