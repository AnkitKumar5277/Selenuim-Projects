import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@allure.title("selenium mini project 2_amazon")
@allure.description("print the items and prices of Mac Mini on Amazon India")
@pytest.mark.itemsandprice
def test_print_items_price_amazon():
    edge_options = Options()
    edge_options.add_argument("--inprivate")
    edge_options.add_argument("--start-maximized")

    driver = webdriver.Edge(options=edge_options)
    driver.get("https://www.amazon.in/")
    time.sleep(3)

    # Search box
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)

    # Get all titles and prices
    titles = driver.find_elements(
        By.XPATH,
        "//div[@data-component-type='s-search-result']//h2"
    )

    prices = driver.find_elements(
        By.XPATH,
        "//div[@data-component-type='s-search-result']//span[@class='a-price-whole']"
    )

    # Collect title-price pairs safely
    # Collect pairs
    items_with_prices = []
    for t, p in zip(titles, prices):
        items_with_prices.append(f"{t.text} - {p.text}")


    # Print all at once
    print("\n=====Your Items and Prices on Amazon India =====")
    for item in items_with_prices:
        print(item)
        print()
    time.sleep(5)
    driver.quit()
