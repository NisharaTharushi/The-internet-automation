from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  

time.sleep(2)

# A/B link find by href
link = driver.find_element(By.XPATH, "//a[@href='/abtest']")
print("A/B link found")
link.click()

time.sleep(2)

# http://elementalselenium.com/ find by href
link = driver.find_element(By.XPATH, "//a[@href='http://elementalselenium.com/']")
print("http://elementalselenium.com/ found")
link.click()

time.sleep(2)

driver.back()

