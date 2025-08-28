# Import tools to control the browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Start Edge browser in private mode
browser = webdriver.Edge()
browser.maximize_window()  # Make browser full-screen

# Step 1: Go to the website
browser.get("https://katalon-demo-cura.herokuapp.com/")

# Step 2: Click "Make Appointment" button
# Wait up to 10 seconds for the button to be clickable
appointment_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "btn-make-appointment"))
)
appointment_button.click()

# Step 3: Log in
# Wait for the username field to appear
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "txt-username")))
# Type username
browser.find_element(By.ID, "txt-username").send_keys("John Doe")
# Type password
browser.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
# Click login button
browser.find_element(By.ID, "btn-login").click()

# Step 4: Fill the appointment form
# Wait for the facility dropdown to appear
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "combo_facility")))
# Choose "Hongkong CURA Healthcare Center" from dropdown
dropdown = Select(browser.find_element(By.ID, "combo_facility"))
dropdown.select_by_visible_text("Hongkong CURA Healthcare Center")

# Check the hospital readmission box
browser.find_element(By.ID, "chk_hospotal_readmission").click()

# Choose "Medicaid" option
browser.find_element(By.CSS_SELECTOR, "input[value='Medicaid']").click()

# Step 5: Pick a date
# Wait for the date field to be clickable
date_input = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "txt_visit_date"))
)
date_input.click()
# Wait for day 30 to be clickable
date_to_select = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//td[text()='30']"))
)
date_to_select.click()

# Step 6: Add a comment
# Wait for the comment box to be ready
comment_box = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "txt_comment"))
)
comment_box.send_keys("Automated appointment")

# Step 7: Book the appointment
# Wait for the book button to be clickable
book_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "btn-book-appointment"))
)
book_button.click()

# Show success message
print("Appointment booked! Closing browser in 5 seconds...")

# Wait 5 seconds, then close browser
time.sleep(5)
browser.quit()
