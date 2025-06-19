from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)


# JavaScript Alerts link find by href
link = driver.find_element(By.LINK_TEXT, "JavaScript Alerts")
link.click()
print("JavaScript Alerts link found and clicked")
time.sleep(2)


# Click for JS Alert button find by xpath
js_alert = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
js_alert.click()
print("JS Alert button found and clicked")

# accept alert
alert = driver.switch_to.alert
alert.accept()

# result find by id
result = driver.find_element(By.ID, "result")
print("result is: " + result.text)
time.sleep(2)

# Click for JS Confirm button find by xpath
js_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
js_confirm.click()
print("JS Confirm button found and clicked")

# dismiss alert
alert = driver.switch_to.alert
alert.dismiss()

# result find by id
result = driver.find_element(By.ID, "result")
print("result is: " + result.text)
time.sleep(2)

# Click for JS Prompt button find by xpath
js_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
js_prompt.click()
print("JS Prompt button found and clicked")

# dismiss alert
alert = driver.switch_to.alert
alert.dismiss()

# result find by id
result = driver.find_element(By.ID, "result")
print("result is: " + result.text)
time.sleep(2)

driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")