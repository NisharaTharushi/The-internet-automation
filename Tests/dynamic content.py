from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  

time.sleep(2)


# Dynamic Content find by href
link = driver.find_element(By.LINK_TEXT, "Dynamic Content")
link.click()
print("Dynamic Content link found and clicked")

time.sleep(2)

# click here find by href
link = driver.find_element(By.XPATH, "//a[@href='/dynamic_content?with_content=static']")
time.sleep(2)

# get href before click
test = link.get_attribute("href")

# click
link.click()
print("Click Here link found and clicked")
# print("link href is: " + test)

time.sleep(2)

if test == "https://the-internet.herokuapp.com/dynamic_content?with_content=static":
    print("Dynamic Content test passed")
else:
    print("Dynamic Content test failed")