from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/exit_intent")
time.sleep(2)


# Move mouse out from flash message
element = driver.find_element(By.ID, "flash-messages")
print("Flash message found")


# Move mouse to the center of the page
actions = ActionChains(driver)
actions.move_by_offset(0, 0).perform()  # Start at current location
time.sleep(1)

# Now move mouse toward top of the window (simulate exit intent)
# Instead of large offset, use smaller values to avoid going out of bounds
actions.move_by_offset(10, -100).perform()
time.sleep(2)

# Wait for modal to appear and close it
try:
    close = driver.find_element(By.XPATH, "//div[@class='modal-footer']/p")
    print("Close button found")
    close.click()
except Exception :
    print("Close button not found or modal did not appear:")

time.sleep(2)