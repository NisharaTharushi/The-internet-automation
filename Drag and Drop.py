from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  

time.sleep(2)

# Drag and Drop link find by href
link = driver.find_element(By.LINK_TEXT, "Drag and Drop")
print("Drag and Drop link found")
link.click()

time.sleep(2)

# find Draggable element by id
draggable = driver.find_element(By.ID, "column-a")
print("Draggable element found")

# find Droppable element by id
droppable = driver.find_element(By.ID, "column-b")
print("Droppable element found")

# drag and drop the draggable element to the droppable element
actions = webdriver.ActionChains(driver)
actions.drag_and_drop(draggable, droppable).perform()

time.sleep(2)

# check if the draggable element has been moved to the droppable element
if draggable.get_attribute("id") == droppable.get_attribute("id"):
    print("Draggable element has been moved to the Droppable element")
else:
    print("Draggable element has not been moved to the Droppable element")

time.sleep(2)

# 