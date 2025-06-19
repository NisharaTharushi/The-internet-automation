from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)



# File Upload link find by href
link = driver.find_element(By.LINK_TEXT, "File Upload")
print("File Upload link found")
link.click()
time.sleep(2)


# File Upload button find by id
file_upload = driver.find_element(By.ID, "file-upload")
file_upload.send_keys("C:\\Users\\User\\Downloads\\learn.jpg")
time.sleep(2)
print("File Upload button found and clicked")


# file-submit" find by id
submit = driver.find_element(By.ID, "file-submit")
submit.click()
print("Submit button found and clicked")
time.sleep(2)
