from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (Chrome in this case)
driver = webdriver.Chrome()

# Open the website
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)

# Entry Ad link
link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Entry Ad")))
print("Entry Ad link found")
link.click()

# Wait for modal and find the Close button
close = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Close']")))
driver.execute_script("arguments[0].scrollIntoView(true);", close)
time.sleep(1)
print("Close button found")
close.click()

# Click the 'Click here' button to show ad again
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "restart-ad")))
button.click()
print("Click Here button found and clicked")
time.sleep(2)

# Wait and click Close again
close = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Close']")))
driver.execute_script("arguments[0].scrollIntoView(true);", close)
time.sleep(1)
print("Close button found")
close.click()

# Close browser (optional)
driver.quit()
