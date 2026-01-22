import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options

@allure.title("Opencart Registration Account Testing With Selenium_Mini_Project 3")
@allure.description("TC1 - Positive TC - Fill the registration form with valid data and verify account creation")
@pytest.mark.positive
def test_awesome_qa():
    # Setup Edge options (optional: run in private mode)
    edge_options = Options()
    # edge_options.add_argument("--inprivate")  # uncomment for private mode
    driver = webdriver.Edge(options=edge_options)

    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    # Fill registration form
    wait.until(EC.presence_of_element_located((By.NAME, "firstname"))).send_keys("Ankit")
    driver.find_element(By.NAME, "lastname").send_keys("Kumar")
    driver.find_element(By.ID, "input-email").send_keys("srt65spr18@gmail.com")
    driver.find_element(By.ID, "input-telephone").send_keys("6829994324")
    driver.find_element(By.NAME, "password").send_keys("Sakhamudi@3001")
    driver.find_element(By.NAME, "confirm").send_keys("Sakhamudi@3001")

    # Accept policy checkbox
    driver.find_element(By.NAME, "agree").click()

    # Click continue
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # Wait for success page
    success_message = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='content']//*[text()='Your Account Has Been Created!']"))
    )

    # Assertions
    assert driver.current_url == "https://awesomeqa.com/ui/index.php?route=account/success"
    assert "Your Account Has Been Created!" in success_message.text

    print("Driver Title:", driver.title)
    print("Success Message:", success_message.text)

    driver.quit()


# pytest -s main.py --alluredir=reports
# allure serve reports
