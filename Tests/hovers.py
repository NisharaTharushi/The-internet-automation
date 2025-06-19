from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  

driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)


# Hovers link find by href
link = driver.find_element(By.LINK_TEXT, "Hovers")
print("Hovers link found")
link.click()
time.sleep(2)


# Hover Over button find by xpath and hover over  
# /img/avatar-blank.jpg find by xpath
image = driver.find_element(By.XPATH, "//img[@src='/img/avatar-blank.jpg']")
image_test = image.get_attribute("src")
print("image 1 found image link is: " + image_test)

# hover over the image
actions = webdriver.ActionChains(driver)
actions.move_to_element(image).perform()
time.sleep(2)
print("image 1 hovered over")


# View profile link find by xpath
link = driver.find_element(By.XPATH, "//a[@href='/users/1']")
link.click()
print("View profile link found and clicked")
time.sleep(2)


# check if the profile page is displayed
if driver.current_url == "https://the-internet.herokuapp.com/users/1":
    print("View profile 1 page open test passed")
else:
    print("View profile 1 test failed")


driver.get('https://the-internet.herokuapp.com/hovers')
time.sleep(2)
print("")