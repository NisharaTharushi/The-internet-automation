from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)


# Geolocation link find by href
link = driver.find_element(By.LINK_TEXT, "Geolocation")
link.click()
print("Geolocation link found and clicked")
time.sleep(2)


# Where am I? find button by text
where_am_i_button = driver.find_element(By.TAG_NAME, "button")
if where_am_i_button.text.strip() == "Where am I?":
    where_am_i_button.click()
    print("Where am I? button clicked")

time.sleep(2)

# click Allow button find by text
allow_button = driver.find_element(By.TAG_NAME, "button")
allow_button.click()
print("Allow button found and clicked")
time.sleep(2)

# check Geolocation page open after click
if driver.current_url == "https://the-internet.herokuapp.com/geolocation":
    print("Geolocation page open and test passed")
else:
    print("Geolocation test failed")


driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")