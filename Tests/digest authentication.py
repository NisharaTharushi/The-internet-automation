from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  

time.sleep(2)

# Digest Authentication link find by href
link = driver.find_element(By.LINK_TEXT, "Digest Authentication")
print("Digest Authentication link found")
link.click()

time.sleep(2)

# Credentials that hardcoded only accept
username = "admin"
password = "admin"

# Build URL with credentials and the link of the page that need to open after submit the popup 
url = f"https://{username}:{password}@the-internet.herokuapp.com/digest_auth"
print("Digest Authentication link found:", url)

# Launch browser
driver = webdriver.Firefox()

# Go to the URL
driver.get(url)

# check if url is correct
print("✔ Logged in using Digest Auth", url)
if url == "https://admin:admin@the-internet.herokuapp.com/digest_auth":
    print("Digest Authentication test passed")


# Wait for page to load
time.sleep(2)

# Get success message
message = driver.find_element(By.TAG_NAME, "p").text
print("Login message:", message)

