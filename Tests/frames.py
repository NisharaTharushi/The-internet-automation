from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)


# Frames link find by href
link = driver.find_element(By.LINK_TEXT, "Frames")
print("Frames link found")
link.click()
time.sleep(2)


# Nested Frames find by href
frame = driver.find_element(By.LINK_TEXT, "Nested Frames")
frame.click()

# check https://the-internet.herokuapp.com/nested_frames page open after click
if driver.current_url == "https://the-internet.herokuapp.com/nested_frames":
    print("nested Frames test passed")
else:
    print("Nested Frames test failed")

driver.get('https://the-internet.herokuapp.com/frames')
time.sleep(2)


# iFrame find by href
frame = driver.find_element(By.LINK_TEXT, "iFrame")
frame.click()

# check https://the-internet.herokuapp.com/iframe page open after click
if driver.current_url == "https://the-internet.herokuapp.com/iframe":
    print("iFrame test passed")
else:
    print("iFrame test failed")

driver.get('https://the-internet.herokuapp.com/iframe')
time.sleep(2)

# Learn more. link find by href
link = driver.find_element(By.LINK_TEXT, "Learn more.")
link.click()
time.sleep(2)

driver.get('https://the-internet.herokuapp.com/iframe')
time.sleep(2)


# tox-icon find by class name
close = driver.find_element(By.CLASS_NAME, "tox-icon")
close.click()
print("Close button found and clicked")

driver.get('https://the-internet.herokuapp.com/')
time.sleep(2)
print("")



