# Import necessary libraries
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Test function for account registration
def test_register_account():
    # Step 1: Launch Edge browser
    driver = webdriver.Edge()
    
    # Step 2: Open the registration page
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    
    # Step 3: Fill in the registration form
    driver.find_element(By.NAME, "firstname").send_keys("Ankit")           # First Name
    driver.find_element(By.NAME, "lastname").send_keys("Kumar")            # Last Name
    driver.find_element(By.ID, "input-email").send_keys("srt65spr18@gmail.com")  # Email
    driver.find_element(By.ID, "input-telephone").send_keys("6829994324")  # Telephone
    driver.find_element(By.NAME, "password").send_keys("Sakhamudi@3001")   # Password
    driver.find_element(By.NAME, "confirm").send_keys("Sakhamudi@3001")    # Confirm Password
    
    # Step 4: Agree to privacy policy
    driver.find_element(By.NAME, "agree").click()
    
    # Step 5: Click the Continue button
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    
    # Step 6: Verify account creation
    assert driver.current_url == "https://awesomeqa.com/ui/index.php?route=account/success"
    
    # Step 7: Print the success message
    success_message = driver.find_element(By.XPATH,
                                          "//div[@id='content']//*[text()='Your Account Has Been Created!']")
    print("Success Message:", success_message.text)
    
    # Step 8: Close the browser
    driver.quit()
