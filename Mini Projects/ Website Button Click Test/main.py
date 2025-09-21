from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure

def test_buttn_click():
    driver = webdriver.Edge()
    try:
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        button = driver.find_element(By.ID, "btn-make-appointment")
        button.click()
        assert "profile.php" in driver.current_url, "URL did not change as expected"

    finally:
        time.sleep(10)
        driver.quit()
