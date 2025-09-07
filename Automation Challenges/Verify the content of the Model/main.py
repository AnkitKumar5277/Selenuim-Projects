import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://demoqa.com/modal-dialogs")

time.sleep(2)
driver.find_element(By.ID, "showLargeModal").click()

time.sleep(2)
modal_title = driver.find_element(By.ID, "example-modal-sizes-title-lg").text
modal_content = driver.find_element(By.CSS_SELECTOR, ".modal-body").text

expected_title = "Large Modal"
expected_text_snippet = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

assert modal_title == expected_title, f"❌ Title mismatch! Got: {modal_title}"
assert expected_text_snippet in modal_content, "❌ Modal content does not match!"

print("✅ Modal content verified successfully!")

# Step 5: Close modal
driver.find_element(By.ID, "closeLargeModal").click()

# Quit browser
time.sleep(2)
driver.quit()
