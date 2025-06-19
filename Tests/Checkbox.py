from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Firefox browser
driver = webdriver.Firefox()

# Step 1: Open the main page
driver.get('https://the-internet.herokuapp.com/')
print("Opened The Internet homepage.")
time.sleep(2)

# Step 2: Navigate to the Checkboxes page
checkbox_link = driver.find_element(By.XPATH, "//a[@href='/checkboxes']")
checkbox_link.click()
print("Navigated to the Checkboxes page.")
time.sleep(2)

# Step 3: Locate all checkboxes on the page
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# Step 4: Toggle each checkbox
for index, checkbox in enumerate(checkboxes, start=1):
    checkbox.click()
    print(f"Checkbox {index} clicked.")
    time.sleep(1)

# Step 5: Go back to the main page
driver.back()
print("Returned to the homepage.")
time.sleep(2)

# Close browser
driver.quit()
print("Test completed and browser closed.")

