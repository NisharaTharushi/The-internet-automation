from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  

time.sleep(2)


# Entry Ad link find by href
link = driver.find_element(By.LINK_TEXT, "Entry Ad")
print("Entry Ad link found")
link.click()

time.sleep(2)

# Close button find by Close p tag
close = driver.find_element(By.XPATH, "//p[text()='Close']")
print("Close button found")
close.click()


# click here button find by id
button = driver.find_element(By.ID, "restart-ad")
button.click()
print("Click Here button found and clicked")

time.sleep(2)

# Close button find by Close p tag
close = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Close']")))
driver.execute_script("arguments[0].scrollIntoView(true);", close)
close.click()
print("Close button found and clicked")
time.sleep(2)
