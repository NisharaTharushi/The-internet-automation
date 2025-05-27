from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)


# Heading element find 
title = driver.find_element(By.CLASS_NAME, "heading")
print("title found")
title_test = title.text
print("title is: " + title_test)


# find https://github.com/tourdedave/the-internet element

github = driver.find_element(By.XPATH, "//a[@href='https://github.com/tourdedave/the-internet']")
print("github found")
github_test = github.get_attribute("href")
print("github link is: " + github_test)
if github_test == "https://github.com/tourdedave/the-internet":
    print("github test passed")
else:
    print("github test failed")


