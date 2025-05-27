from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)


# Infinite Scroll link find by href
link = driver.find_element(By.LINK_TEXT, "Infinite Scroll")
print("Infinite Scroll link found")
link.click()
time.sleep(2)


# scroll down 5 times
for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
print("Infinite Scroll test passed")