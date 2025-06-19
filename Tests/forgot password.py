from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  

driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)



# Forgot Password link find by href
link = driver.find_element(By.LINK_TEXT, "Forgot Password")
print("Forgot Password link found")
link.click()
time.sleep(2)


# Email field find by id
email = driver.find_element(By.ID, "email")
print("Email field found")
email.send_keys("4qY6M@example.com")
time.sleep(2)

# Reset Password button find by id form_submit
reset = driver.find_element(By.ID, "form_submit")
reset.click()
print("Reset Password button found and clicked")
time.sleep(2)


driver.get('https://the-internet.herokuapp.com/')  
print("")