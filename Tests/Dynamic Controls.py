from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  

time.sleep(2)

# Dynamic Controls find by href
link = driver.find_element(By.LINK_TEXT, "Dynamic Controls")
link.click()
print("Dynamic Controls link found and clicked")

time.sleep(2)

# checkbox find by id
checkbox = driver.find_element(By.ID, "checkbox")
checkbox.click()
print("Checkbox found and clicked")

time.sleep(2)

# Remove button find by xpath
remove = driver.find_element(By.XPATH, "//button[@onclick='swapCheckbox()']")
remove.click()
print("Remove button found and clicked")

time.sleep(2)

# Add button find by xpath
add = driver.find_element(By.XPATH, "//button[@onclick='swapCheckbox()']")
add.click()
print("Add button found and clicked")

time.sleep(2)

# Enable button find by xpath
enable = driver.find_element(By.XPATH, "//button[@onclick='swapCheckbox()']")
enable.click()
print("Enable button found and clicked")

time.sleep(2)

# Disable button find by xpath
disable = driver.find_element(By.XPATH, "//button[@onclick='swapCheckbox()']")
disable.click()
print("Disable button found and clicked")

time.sleep(2)

