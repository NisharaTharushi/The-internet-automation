from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  

time.sleep(2)

# Checkbox link find by href
link = driver.find_element(By.XPATH, "//a[@href='/checkboxes']")
print("Checkbox link found")
link.click()

time.sleep(2)

# find  checkbox 1 by visible text
checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
checkbox.click()
print("Checkbox 1 found and clicked")

time.sleep(2)

# find  checkbox 2 by visible text
checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox' and @checked]")
checkbox.click()
print("Checkbox 2 found and clicked")

time.sleep(2)

driver.back()
time.sleep(2)


