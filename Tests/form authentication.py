from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)


# Form Authentication link find by href
link = driver.find_element(By.LINK_TEXT, "Form Authentication")
print("Form Authentication link found")
link.click()
time.sleep(2)


# Username field find by id
username = driver.find_element(By.ID, "username")
print("Username field found")
username.send_keys("tomsmith")
time.sleep(2)


# Password field find by id
password = driver.find_element(By.ID, "password")
print("Password field found")
password.send_keys("SuperSecretPassword!")
time.sleep(2)


# Login button find by type submit
login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login.click()
print("Login button found and clicked")
time.sleep(2)


# Logout link find by href
logout = driver.find_element(By.LINK_TEXT, "Logout")
logout.click()
print("Logout link found and clicked")
time.sleep(2)


driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")
