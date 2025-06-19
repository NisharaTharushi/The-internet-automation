from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  

time.sleep(2)

# Add/Remove Elements link find by href
link = driver.find_element(By.XPATH, "//a[@href='/add_remove_elements/']")
print("Add/Remove Elements link found")
link.click()

time.sleep(2)

# Add Element button find by xpath
add = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
print("Add Element button found")
add.click()

time.sleep(2)

# Delete Element button find by xpath
delete = driver.find_element(By.XPATH, "//button[@onclick='deleteElement()']")
print("Delete Element button found")
delete.click()

time.sleep(2)

driver.back()