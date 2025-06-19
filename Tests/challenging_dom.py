from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  

time.sleep(2)

# challenging_dom link find by href
link = driver.find_element(By.XPATH, "//a[@href='/challenging_dom']")
print("challenging_dom link found")
link.click()

time.sleep(2)


# bar button find by class button
bar = driver.find_element(By.CLASS_NAME, "button")
bar.click()
print("bar button found and clicked ")
time.sleep(2)

# qux button find by id
qux = driver.find_element(By.XPATH, "//a[contains(@class, 'button') and contains(@class, 'alert')]")
qux.click()
print("qux button found and clicked ")
time.sleep(2)

# bax find by id
bax = driver.find_element(By.XPATH, "//a[contains(@class, 'button') and contains(@class, 'success')]")
bax.click()
print("bax button found and clicked ")
time.sleep(2)


# Table 
# find large-10 columns table by class
table = driver.find_element(By.CLASS_NAME, "large-10.columns")
table_test = table.text
print("table found and table is: " + table_test)

time.sleep(2)


# edit button 
# find all edit buttons by href in the table and assign to edit_b variable
edit_button = table.find_elements(By.XPATH, "//a[@href='#edit']")

# loop through all edit buttons
for edit_button in edit_button:
    edit_button.click()  # Click the Edit button
    print("✅ Edit button found and clicked")


# find all delete buttons by href in the table and assign to delete_b variable
delete_button = table.find_elements(By.XPATH, "//a[@href='#delete']")

# loop through all delete buttons
for delete_button in delete_button:
    delete_button.click()  # Click the Delete button
    print("✅ Delete button found and clicked")

time.sleep(2)


# canvas find by id
canvas = driver.find_element(By.ID, "canvas")
text = canvas.text
print("canvas found and clicked", text)
time.sleep(2)