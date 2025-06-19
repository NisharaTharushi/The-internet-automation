from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  

driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  



# Dynamically Loaded Content link find by href
link = driver.find_element(By.LINK_TEXT, "Dynamic Loading")
print("Dynamically Loaded Content link found")
link.click()

time.sleep(2)


# Example 1: Element on page that is hidden 
link = driver.find_element(By.LINK_TEXT, "Example 1: Element on page that is hidden")
print("Example 1: Element on page that is hidden link found")
link.click()

time.sleep(2)

# start button find by id
start = driver.find_element(By.ID, "start")
start.click()
print("Start button found and clicked")

time.sleep(2)

# Hello World! find by id
hello = driver.find_element(By.ID, "finish")
time.sleep(2)

test_hello = hello.get_attribute("innerText")
print("Hello World! appears.")
print("button text:",test_hello)

time.sleep(2)
driver.back()


# Example 2: Element rendered after the fact
link = driver.find_element(By.LINK_TEXT, "Example 2: Element rendered after the fact")
print("Example 2: Element rendered after the fact link found")
link.click()
time.sleep(2)

# start button find by id
start = driver.find_element(By.ID, "start")
start.click()
print("Start button found and clicked")
time.sleep(4)


# Hello World! find by id
# # Wait for "Hello World!" text to appear
# try:
#     hello = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
#     test_hello = hello.text
#     print("Hello World! appears. button text:", test_hello)
# except Exception as e:
#     print("Error occurred:", str(e))
#     driver.quit()

