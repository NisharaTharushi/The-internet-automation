from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  

time.sleep(2)


# Dropdown element find by href
link = driver.find_element(By.LINK_TEXT, "Dropdown")
link.click()
print("Dropdown link found and clicked")

time.sleep(2)


# dropdown button find by id
dropdown = driver.find_element(By.ID, "dropdown")
dropdown.click()
print("Dropdown button found and clicked")

time.sleep(2)

# Select Option 1 by value 1
option1 = driver.find_element(By.XPATH, "//option[@value='1']")
option1.click()
print("✔ Option 1 is selected")

time.sleep(2)

# Select Option 2 by value 2
option2 = driver.find_element(By.XPATH, "//option[@value='2']")
option2.click()
print("✔ Option 2 is selected")

time.sleep(2)

