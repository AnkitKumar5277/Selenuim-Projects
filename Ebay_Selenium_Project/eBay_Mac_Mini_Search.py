import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


@allure.title("selenium mini project 2_ebay")
@allure.description("print the items and prices of Macmini")
@pytest.mark.itemsandprice
def test_print_items_price():
    edge_options = Options()
    edge_options.add_argument("--inprivate")
    edge_options.add_argument("--start-maximized")

    driver = webdriver.Edge(options=edge_options)
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    time.sleep(2)

    search_box = driver.find_element(By.XPATH, "//input[starts-with(@id,'gh')]")
    search_box.send_keys("macmini")

    search_button_web_element = driver.find_element(By.XPATH, "//span[@class='gh-search-button__label']")
    search_button_web_element.click()
    time.sleep(2)

    # Get all titles and prices
    titles = driver.find_elements(By.XPATH, "//div[@class='s-item__title']")
    prices = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")

    # Collect pairs
    items_with_prices = []
    for t, p in zip(titles, prices):
        items_with_prices.append(f"{t.text} - {p.text}")

    # Print all at once in the end
    print("\n===== Mac Mini Items and Prices on eBay =====")
    for item in items_with_prices:
        print(item)

    time.sleep(5)
    driver.quit()
