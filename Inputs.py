from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)

# Inputs link find by href
link = driver.find_element(By.LINK_TEXT, "Inputs")
link.click()
time.sleep(2) 


# Input element find by xpath
input = driver.find_element(By.XPATH, "//input[@type='number']")
print("Input field found")

input.send_keys("22")
print("Input element value is: " + input.get_attribute("value"))
time.sleep(2)


