from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)



# Horizontal Slider link find by href
link = driver.find_element(By.LINK_TEXT, "Horizontal Slider")
print("Horizontal Slider link found")
link.click()
time.sleep(2)


# range slider find by xpath
slider = driver.find_element(By.XPATH, "//input[@type='range']")
print("range slider found")

# Move the slider to the right to reach value 3.0 (starting at 0, step is 0.5)
steps = int((3.0 - 0.0) / 0.5)
for _ in range(steps):
    slider.send_keys(Keys.ARROW_RIGHT)
    time.sleep(0.2)  # small delay to let UI update


# print the value of the slider
print(slider.get_attribute("value"))
time.sleep(2)