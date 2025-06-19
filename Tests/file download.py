from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")



# File Download link find by href
link = driver.find_element(By.LINK_TEXT, "File Download")
link.click()
print("File Download link found")
time.sleep(2)


# learn.jpg find by href
link = driver.find_element(By.LINK_TEXT, "learn.jpg")
link.click()
print("learn.jpg link found and clicked")
time.sleep(2)

# file_example_XLSX_5000.xlsx find by href
link = driver.find_element(By.LINK_TEXT, "file_example_XLSX_5000.xlsx")
link.click()
print("file_example_XLSX_5000.xlsx link found and clicked")

# random_data.txt find by href
link = driver.find_element(By.LINK_TEXT, "random_data.txt")
link.click()
print("random_data.txt link found and clicked")

# images.jpeg find by href
link = driver.find_element(By.LINK_TEXT, "images.jpeg")
link.click()
print("images.jpeg link found and clicked")

time.sleep(2)
driver.back()
time.sleep(2)
