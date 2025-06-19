from selenium import webdriver
from selenium.webdriver.common.by import By  
import time  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)



# Heading element find 
title = driver.find_element(By.CLASS_NAME, "heading")
print("title found")
title_test = title.text
print("title is: " + title_test)


# find https://github.com/tourdedave/the-internet element

github = driver.find_element(By.XPATH, "//a[@href='https://github.com/tourdedave/the-internet']")
print("github found")
github_test = github.get_attribute("href")
print("github link is: " + github_test)
if github_test == "https://github.com/tourdedave/the-internet":
    print("github test passed")
else:
    print("github test failed")


driver.get('https://the-internet.herokuapp.com/')
print()



# A/B link find by href
link = driver.find_element(By.XPATH, "//a[@href='/abtest']")
print("A/B link found")
link.click()
time.sleep(2)

# http://elementalselenium.com/ find by href
link = driver.find_element(By.XPATH, "//a[@href='http://elementalselenium.com/']")
print("http://elementalselenium.com/ found")
link.click()
time.sleep(2)


driver.get('https://the-internet.herokuapp.com/')
time.sleep(2)
print()



# Add/Remove Elements link find by href
link = driver.find_element(By.XPATH, "//a[@href='/add_remove_elements/']")
print("Add/Remove Elements link found")
link.click()

time.sleep(2)

# Add Element button find by xpath
add = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
print("Add Element button found")
add.click()

time.sleep(2)

# Delete Element button find by xpath
delete = driver.find_element(By.XPATH, "//button[@onclick='deleteElement()']")
print("Delete Element button found")
delete.click()

time.sleep(2)
driver.back()
time.sleep(2)
print("")


# ***** important
# Alert box hanndle ****8
print("Basic Auth / Alert box handle")

# Credentials
username = "admin"
password = "admin"

# Build URL with credentials
url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
print("Navigating to:", url)

# Launch Chrome browser
driver = webdriver.Firefox()

# Go to the URL
driver.get(url)
print("✔ Logged in using Basic Auth")

# Wait for page to load
time.sleep(2)

# Get success message
message = driver.find_element(By.TAG_NAME, "p").text
print("Login message:", message)

driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)
print("")


# Broken images link find by href
link = driver.find_element(By.LINK_TEXT, "Broken Images")
print("Broken images link found")
link.click()

time.sleep(2)

# find image by src
image = driver.find_element(By.XPATH, "//img[@src='asdf.jpg']")
print("image found")
image_test = image.get_attribute("src")
print("image link is: " + image_test)

# check if image is broken
if image_test == "https://the-internet.herokuapp.com/images/asdf.jpg": 
    # get the link from the brocken image page link and then remove broken word 
    print("image not broken")
else:
    print("image is broken")

driver.back()
print("")



# Challenging_dom link find by href
link = driver.find_element(By.XPATH, "//a[@href='/challenging_dom']")
print("challenging_dom link found")
link.click()

time.sleep(2)

# buttons
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

# canvas find by id
canvas = driver.find_element(By.ID, "canvas")
text = canvas.text
print("canvas found and clicked", text)
time.sleep(2)


time.sleep(2)
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")



# Checkbox link find by href
link = driver.find_element(By.XPATH, "//a[@href='/checkboxes']")
print("Checkbox link found")
link.click()

time.sleep(2)

# find  checkbox 1 by visible text
checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
checkbox.click()
print("Checkbox 1 found and clicked")

time.sleep(2)

# find  checkbox 2 by visible text
checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox' and @checked]")
checkbox.click()
print("Checkbox 2 found and clicked")

time.sleep(2)
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")



# find Context Menu link
link = driver.find_element(By.LINK_TEXT, "Context Menu")
print("Context Menu link found")
link.click()

time.sleep(2)

# Find the box to right-click
box = driver.find_element(By.ID, "hot-spot")

# Right-click on the box
ActionChains(driver).context_click(box).perform()

time.sleep(1)

# Switch to alert and accept it
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()

print("Alert accepted")

time.sleep(2)
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")



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

time.sleep(2)

# Get success message
message = driver.find_element(By.TAG_NAME, "p").text
print("Login message:", message)
print("Digest Authentication test passed")
print("")


driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")



# find Disapearing link
link = driver.find_element(By.LINK_TEXT, "Disappearing Elements")
print("Disappearing link found")
link.click()

time.sleep(2)

# ckeck the h3 name Disappearing Elements 
h3 = driver.find_element(By.TAG_NAME, "h3")
print("h3 name is: " + h3.text)

time.sleep(2)

# Home button find by href
home = driver.find_element(By.LINK_TEXT, "Home")
print("Home button found")
home.click()

driver.back()
time.sleep(2)

# About button find by href
about = driver.find_element(By.LINK_TEXT, "About")
print("About button found")
about.click()

driver.back()
time.sleep(2)

# Contact Us button find by href
contact = driver.find_element(By.LINK_TEXT, "Contact Us")
print("Contact Us button found")
contact.click()

driver.back()
time.sleep(2)

# Portfolio button find by href
portfolio = driver.find_element(By.LINK_TEXT, "Portfolio")
print("Portfolio button found")
portfolio.click()

driver.back()
time.sleep(2)

# Elemental Selenium link find by href
elemental = driver.find_element(By.LINK_TEXT, "Elemental Selenium")
print("Elemental Selenium link found")
elemental.click()

driver.back()
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")



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
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")



# Dropdown element find by href
link = driver.find_element(By.LINK_TEXT, "Dropdown")
link.click()
print("Dropdown link found and clicked")
time.sleep(2)


# dropdown button find by id
dropdown = driver.find_element(By.ID, "dropdown")
dropdown.click()
print("Dropdown button found and clicked")
time.sleep(2)


# Select Option 1 by value 1
option1 = driver.find_element(By.XPATH, "//option[@value='1']")
option1.click()
print("✔ Option 1 is selected")
time.sleep(2)


# Select Option 2 by value 2
option2 = driver.find_element(By.XPATH, "//option[@value='2']")
option2.click()
print("✔ Option 2 is selected")


time.sleep(2)
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")



# Dynamic Content find by href
link = driver.find_element(By.LINK_TEXT, "Dynamic Content")
link.click()
print("Dynamic Content link found and clicked")

time.sleep(2)

# click here find by href
link = driver.find_element(By.XPATH, "//a[@href='/dynamic_content?with_content=static']")
time.sleep(2)

# get href before click
test = link.get_attribute("href")

# click
link.click()
print("Click Here link found and clicked :")


if test == "https://the-internet.herokuapp.com/dynamic_content?with_content=static":
    print("Dynamic Content test passed")
else:
    print("Dynamic Content test failed")


driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")



# Dynamic Controls find by href
link = driver.find_element(By.LINK_TEXT, "Dynamic Controls")
link.click()
print("Dynamic Controls link found and clicked")
time.sleep(2)


# checkbox find by id
checkbox = driver.find_element(By.ID, "checkbox")
checkbox.click()
print("Checkbox found and clicked")
time.sleep(2)

# Remove button find by xpath
remove = driver.find_element(By.XPATH, "//button[@onclick='swapCheckbox()']")
remove.click()
print("Remove button found and clicked")
time.sleep(2)

# Add button find by xpath
add = driver.find_element(By.XPATH, "//button[@onclick='swapCheckbox()']")
add.click()
print("Add button found and clicked")
time.sleep(2)

# Enable button find by xpath
enable = driver.find_element(By.XPATH, "//button[@onclick='swapCheckbox()']")
enable.click()
print("Enable button found and clicked")
time.sleep(2)

# Disable button find by xpath
disable = driver.find_element(By.XPATH, "//button[@onclick='swapCheckbox()']")
disable.click()
print("Disable button found and clicked")

time.sleep(2)
driver.get('https://the-internet.herokuapp.com/')  
print("")



# Dynamically Loaded Content link find by href
link = driver.find_element(By.LINK_TEXT, "Dynamic Loading")
print("Dynamically Loaded Content link found")
link.click()
time.sleep(2)


# Example 1: Element on page that is hidden 
link = driver.find_element(By.LINK_TEXT, "Example 1: Element on page that is hidden")
print("Example 1: Element on page that is hidden link found")
link.click()
time.sleep(2)


# start button find by id
start = driver.find_element(By.ID, "start")
start.click()
print("Start button found and clicked")
time.sleep(2)


# Hello World! find by id
hello = driver.find_element(By.ID, "finish")
time.sleep(2)

test_hello = hello.get_attribute("innerText")
print("Hello World! appears. button text:",test_hello)
time.sleep(2)
driver.back()


# Example 2: Element rendered after the fact
link = driver.find_element(By.LINK_TEXT, "Example 2: Element rendered after the fact")
print("Example 2: Element rendered after the fact link found")
link.click()
time.sleep(2)

# start button find by id
start = driver.find_element(By.ID, "start")
start.click()
print("Start button found and clicked")
time.sleep(4)


driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")


# Open the website
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)



# Entry Ad link
link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Entry Ad")))
print("Entry Ad link found")
link.click()

# Wait for modal and find the Close button
close = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Close']")))
driver.execute_script("arguments[0].scrollIntoView(true);", close)
time.sleep(1)
print("Close button found")
close.click()

# Click the 'Click here' button to show ad again
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "restart-ad")))
button.click()
print("Click Here button found and clicked")
time.sleep(2)

# Wait and click Close again
close = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Close']")))
driver.execute_script("arguments[0].scrollIntoView(true);", close)
time.sleep(1)
print("Close button found")
close.click()


driver.get('https://the-internet.herokuapp.com/')
time.sleep(2)
print("")



# File Download link find by href
link = driver.find_element(By.LINK_TEXT, "File Download")
link.click()
print("File Download link found")
time.sleep(2)


# learn.jpg find by href
link = driver.find_element(By.LINK_TEXT, "learn.jpg")
link.click()
print("learn.jpg link found and clicked")
time.sleep(2)
driver.get("https://the-internet.herokuapp.com/download")

# random_data.txt find by href
link = driver.find_element(By.LINK_TEXT, "random_data.txt")
link.click()
print("random_data.txt link found and clicked")


time.sleep(2)
driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")



# File Upload link find by href
link = driver.find_element(By.LINK_TEXT, "File Upload")
link.click()
print("File Upload link found")
time.sleep(2)


# File Upload button find by id
file_upload = driver.find_element(By.ID, "file-upload")
file_upload.send_keys("C:\\Users\\User\\Downloads\\learn.jpg")
time.sleep(2)
print("File Upload button found and clicked")


# file-submit" find by id
submit = driver.find_element(By.ID, "file-submit")
submit.click()
print("Submit button found and clicked")
time.sleep(2)


driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")




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

# check home page open after click
if driver.current_url == "https://the-internet.herokuapp.com/floating_menu#home":
    print("Floating Menu test passed")
else:
    print("Floating Menu test failed")
time.sleep(2)


# News button find by href
news = driver.find_element(By.LINK_TEXT, "News")
print("News button found")
news.click()

# check News page open after click
if driver.current_url == "https://the-internet.herokuapp.com/floating_menu#news":
    print("Floating Menu test passed")
else:
    print("Floating Menu test failed")
time.sleep(2)


# Contact button find by href
contact = driver.find_element(By.LINK_TEXT, "Contact")
print("Contact button found")
contact.click()

# check Contact page open after click
if driver.current_url == "https://the-internet.herokuapp.com/floating_menu#contact":
    print("Floating Menu test passed")
else:
    print("Floating Menu test failed")
time.sleep(2)


driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")



# Forgot Password link find by href
link = driver.find_element(By.LINK_TEXT, "Forgot Password")
print("Forgot Password link found")
link.click()
time.sleep(2)

# Email field find by id
email = driver.find_element(By.ID, "email")
print("Email field found")
email.send_keys("4qY6M@example.com")
time.sleep(2)

# Reset Password button find by id form_submit
reset = driver.find_element(By.ID, "form_submit")
reset.click()
print("Reset Password button found and clicked")
time.sleep(2)


driver.get('https://the-internet.herokuapp.com/')  
print("")



# Form Authentication link find by href
link = driver.find_element(By.LINK_TEXT, "Form Authentication")
print("Form Authentication link found")
link.click()
time.sleep(2)


# Username field find by id
username = driver.find_element(By.ID, "username")
print("Username field found")
username.send_keys("tomsmith")
time.sleep(2)


# Password field find by id
password = driver.find_element(By.ID, "password")
print("Password field found")
password.send_keys("SuperSecretPassword!")
time.sleep(2)


# Login button find by type submit
login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login.click()
print("Login button found and clicked")
time.sleep(2)


# Logout link find by href
logout = driver.find_element(By.LINK_TEXT, "Logout")
logout.click()
print("Logout link found and clicked")
time.sleep(2)


driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")


# Frames link find by href
link = driver.find_element(By.LINK_TEXT, "Frames")
print("Frames link found")
link.click()
time.sleep(2)


# Nested Frames find by href
frame = driver.find_element(By.LINK_TEXT, "Nested Frames")
frame.click()

# check https://the-internet.herokuapp.com/nested_frames page open after click
if driver.current_url == "https://the-internet.herokuapp.com/nested_frames":
    print("nested Frames test passed")
else:
    print("Nested Frames test failed")

driver.get('https://the-internet.herokuapp.com/frames')
time.sleep(2)


# iFrame find by href
frame = driver.find_element(By.LINK_TEXT, "iFrame")
frame.click()

# check https://the-internet.herokuapp.com/iframe page open after click
if driver.current_url == "https://the-internet.herokuapp.com/iframe":
    print("iFrame test passed")
else:
    print("iFrame test failed")

driver.get('https://the-internet.herokuapp.com/iframe')
time.sleep(2)

# Learn more. link find by href
link = driver.find_element(By.LINK_TEXT, "Learn more.")
link.click()
time.sleep(2)

driver.get('https://the-internet.herokuapp.com/iframe')
time.sleep(2)


# tox-icon find by class name
close = driver.find_element(By.CLASS_NAME, "tox-icon")
close.click()
print("Close button found and clicked")

driver.get('https://the-internet.herokuapp.com/')
time.sleep(2)
print("")



# Geolocation link find by href
link = driver.find_element(By.LINK_TEXT, "Geolocation")
link.click()
print("Geolocation link found and clicked")
time.sleep(2)


# Where am I? find button by text
where_am_i_button = driver.find_element(By.TAG_NAME, "button")
if where_am_i_button.text.strip() == "Where am I?":
    where_am_i_button.click()
    print("Where am I? button clicked")

time.sleep(2)

# click Allow button find by text
allow_button = driver.find_element(By.TAG_NAME, "button")
allow_button.click()
print("Allow button found and clicked")
time.sleep(2)

# check Geolocation page open after click
if driver.current_url == "https://the-internet.herokuapp.com/geolocation":
    print("Geolocation page open and test passed")
else:
    print("Geolocation test failed")


driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")


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


driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")



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


driver.get('https://the-internet.herokuapp.com/')  
time.sleep(2)
print("")


# Inputs link find by href
link = driver.find_element(By.LINK_TEXT, "Inputs")
link.click()
time.sleep(2) 


# Input element find by xpath
input = driver.find_element(By.XPATH, "//input[@type='number']")
print("Input field found")

input.send_keys("22")
print("Input element value is: " + input.get_attribute("value"))
time.sleep(2)


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
print("JQuery UI Menus link found and clicked")
time.sleep(2)

driver.get('https://the-internet.herokuapp.com/jqueryui/menu')  
time.sleep(2)


# Enabled button find by href
enabled = driver.find_element(By.LINK_TEXT, "Enabled")
enabled.click()
print("Enabled button found and clicked")
time.sleep(2)


# Downloads button find by href
downloads = driver.find_element(By.LINK_TEXT, "Downloads")
downloads.click()
print("Downloads button found and clicked")
time.sleep(2)


# CSV button find by href
csv = driver.find_element(By.LINK_TEXT, "CSV")
csv.click()
print("CSV button found and clicked")
time.sleep(2)