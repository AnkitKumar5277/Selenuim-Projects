import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Open the browser and go to the website
driver = webdriver.Edge()   # You can also use webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/modal-dialogs")

# Step 2: Click on the 'Large Modal' button
time.sleep(2)  # wait for page to load
large_modal_button = driver.find_element(By.ID, "showLargeModal")
large_modal_button.click()

# Step 3: Get the title and body text of the modal
time.sleep(2)  # wait for modal to appear
modal_title = driver.find_element(By.ID, "example-modal-sizes-title-lg").text
modal_body = driver.find_element(By.CSS_SELECTOR, ".modal-body").text

# Step 4: Verify the content
expected_title = "Large Modal"
expected_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

if modal_title == expected_title and expected_text in modal_body:
    print("✅ Modal content is correct")
else:
    print("❌ Modal content is NOT correct")

# Step 5: Close the modal
close_button = driver.find_element(By.ID, "closeLargeModal")
close_button.click()

# Step 6: Quit the browser
time.sleep(2)
driver.quit()
