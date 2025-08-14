import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

@allure.title("Opencart Registration Account Testing with selenium_mini_project 3")
@allure.description("TC1 - positive TC - fill the registration form with valid data verify whether account created")
@pytest.mark.Positive
def test_awesome_qa():
    driver = webdriver.Edge()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    time.sleep(1)
    # firstname element
    ele_firstname = driver.find_element(By.XPATH, "//input[@name='firstname']")
    ele_firstname.send_keys("Ankit")

    time.sleep(1)
    # lastname element
    ele_lastname = driver.find_element(By.XPATH, "//input[@name='lastname']")
    ele_lastname.send_keys("Kumar")

    time.sleep(1)
    # e-mail element
    ele_email = driver.find_element(By.XPATH, "//input[@id='input-email']")
    ele_email.send_keys("ankitx66@gmail.com")

    time.sleep(1)
    # mobile number
    ele_telephone = driver.find_element(By.XPATH, "//input[@id='input-telephone']")
    ele_telephone.send_keys("9389715277")

    time.sleep(1)
    # password
    ele_password = driver.find_element(By.XPATH, "//input[@name='password']")
    ele_password.send_keys("Sakhamudi@3001")

    time.sleep(1)
    # confirm password
    ele_confirm_password = driver.find_element(By.XPATH, "//input[@name='confirm']")
    ele_confirm_password.send_keys("Sakhamudi@3001")

    time.sleep(5)
    # policy checkbox
    policy_checkbox = driver.find_element(By.XPATH, "//input[@name='agree']")
    policy_checkbox.click()

    # continue button
    continue_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    continue_button.click()

    time.sleep(5)
    assert driver.current_url == "https://awesomeqa.com/ui/index.php?route=account/success"
    time.sleep(5)

    print("Driver Title " + driver.title)

    message_web_element = driver.find_element(By.XPATH, "//div[@id='content']//*[text()='Your Account Has Been Created!']")
    print(message_web_element.text)

    time.sleep(5)
    driver.quit()

 # pytest -s Selenium_Project3.py --alluredir=./allure-results
