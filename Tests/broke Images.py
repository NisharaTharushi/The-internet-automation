from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  

time.sleep(2)

# Broken images link find by href
link = driver.find_element(By.LINK_TEXT, "Broken Images")
print("Broken images link found")
link.click()

time.sleep(2)

# find image by src
image = driver.find_element(By.XPATH, "//img[@src='asdf.jpg']")
print("image found")
image_test = image.get_attribute("src")
print("image link is: " + image_test)

# check if image is broken
if image_test == "https://the-internet.herokuapp.com/images/asdf.jpg": 
    # get the link from the brocken image page link and then remove broken word 
    print("image not broken")
else:
    print("image is broken")
