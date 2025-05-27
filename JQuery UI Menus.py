from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  

driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)


# JQuery UI Menus link find by href
link = driver.find_element(By.LINK_TEXT, "JQuery UI Menus")
link.click()
print("JQuery UI Menus link found and clicked")
time.sleep(2)


# JQuery UI Menus link find by href
link = driver.find_element(By.LINK_TEXT, "JQuery UI Menus")
link.click()
print("JQuery UI Menus link in the page found and clicked")
time.sleep(2)

driver.get('https://the-internet.herokuapp.com/jqueryui/menu')  
time.sleep(2)

# actions
actions = webdriver.ActionChains(driver)

# PDF file test 

# Enabled button find by href
enabled = driver.find_element(By.LINK_TEXT, "Enabled")
actions.move_to_element(enabled).perform()
print("PDF file test")
print("Enabled button found and clicked")
time.sleep(2)


# Downloads button find by href
downloads = driver.find_element(By.LINK_TEXT, "Downloads")
actions.move_to_element(downloads).perform()
print("Downloads button found and clicked")
time.sleep(2)


# PDF button find by href
PDF = driver.find_element(By.LINK_TEXT, "PDF")
PDF.click()
print("PDF button found and clicked")
time.sleep(2)


driver.get('https://the-internet.herokuapp.com/jqueryui/menu')  
time.sleep(2)
print("")


# CSV file test

# Enabled button find by href
enabled = driver.find_element(By.LINK_TEXT, "Enabled")
actions.move_to_element(enabled).perform()
print("CSV file test")
print("Enabled button found and clicked")
time.sleep(2)


# Downloads button find by href
downloads = driver.find_element(By.LINK_TEXT, "Downloads")
actions.move_to_element(downloads).perform()
print("Downloads button found and clicked")
time.sleep(2)


# CSV button find by href
csv = driver.find_element(By.LINK_TEXT, "CSV")
csv.click()
print("CSV button found and clicked")
time.sleep(2)

driver.get('https://the-internet.herokuapp.com/jqueryui/menu')  
time.sleep(2)
print("")


# Excel file test
print("Excel file test")

# Enabled button find by href
enabled = driver.find_element(By.LINK_TEXT, "Enabled")
actions.move_to_element(enabled).perform()
print("Enabled button found and clicked")
time.sleep(2)


# Downloads button find by href
downloads = driver.find_element(By.LINK_TEXT, "Downloads")
actions.move_to_element(downloads).perform()
print("Downloads button found and clicked")
time.sleep(2)


# Excel button find by href
excel = driver.find_element(By.LINK_TEXT, "Excel")
actions.move_to_element(excel).perform()
print("Excel button found and clicked")
time.sleep(2)

driver.get('https://the-internet.herokuapp.com/jqueryui/menu')  
time.sleep(2)
print("")


# Back to JQuery UI test 
print("Back to JQuery UI test")

# Enabled button find by href
enabled = driver.find_element(By.LINK_TEXT, "Enabled")
actions.move_to_element(enabled).perform()
print("Enabled button found and clicked")
time.sleep(2)


# Back to JQuery UI button find by href
back = driver.find_element(By.LINK_TEXT, "Back to JQuery UI")
back.click()
print("Back to JQuery UI button found and clicked")
time.sleep(2)
print("JQuery UI page open test passed")


# JQuery UI us link find by href
print("JQuery UI link test")
link = driver.find_element(By.LINK_TEXT, "JQuery UI")
link.click()
print("JQuery UI link found and clicked")
time.sleep(2)

driver.get('https://the-internet.herokuapp.com/jqueryui')  
time.sleep(2)
print("")


# Menu link find by href
print("Menu link test")
link = driver.find_element(By.LINK_TEXT, "Menu")
link.click()
print("Menu link found and clicked")
time.sleep(2)


driver.get('https://the-internet.herokuapp.com')  
time.sleep(2)
print("")

driver.close()