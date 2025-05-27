from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Open browser and navigate to the site
driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/")

time.sleep(2)

# find Context Menu link
link = driver.find_element(By.LINK_TEXT, "Context Menu")
print("Context Menu link found")
link.click()

time.sleep(2)

# Find the box to right-click
box = driver.find_element(By.ID, "hot-spot")

# Right-click on the box
ActionChains(driver).context_click(box).perform()

time.sleep(1)

# Switch to alert and accept it
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()

print("Alert accepted")


