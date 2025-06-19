from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  

# Credentials that hardcoded only accept
username = "admin"
password = "admin"

# Build URL with credentials
url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
print("Navigating to:", url)

# Launch Chrome browser
driver = webdriver.Chrome()

# Go to the URL
driver.get(url)
print("✔ Logged in using Basic Auth")

# Wait for page to load
time.sleep(2)

# Get success message
message = driver.find_element(By.TAG_NAME, "p").text
print("Login message:", message)

# Optional: driver.quit()
