from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)



# Floating Menu link find by href
link = driver.find_element(By.LINK_TEXT, "Floating Menu")
print("Floating Menu link found")
link.click()
time.sleep(2)


# Floating Menu button find by id
button = driver.find_element(By.ID, "menu")
button.click()
print("Floating Menu button found and clicked")
time.sleep(2)


# Home button find by href
home = driver.find_element(By.LINK_TEXT, "Home")
print("Home button found")
home.click()

# check page open after click
if driver.current_url == "https://the-internet.herokuapp.com/floating_menu#home":
    print("Floating Menu test passed")
else:
    print("Floating Menu test failed")
time.sleep(2)


# News button find by href
news = driver.find_element(By.LINK_TEXT, "News")
print("News button found")
news.click()

# check page open after click
if driver.current_url == "https://the-internet.herokuapp.com/floating_menu#news":
    print("Floating Menu test passed")
else:
    print("Floating Menu test failed")
time.sleep(2)


# Contact button find by href
contact = driver.find_element(By.LINK_TEXT, "Contact")
print("Contact button found")
contact.click()

# check page open after click
if driver.current_url == "https://the-internet.herokuapp.com/floating_menu#contact":
    print("Floating Menu test passed")
else:
    print("Floating Menu test failed")
time.sleep(2)    