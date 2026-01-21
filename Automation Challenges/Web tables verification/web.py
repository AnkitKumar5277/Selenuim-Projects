import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://demoqa.com/webtables")

driver.execute_script("window.scrollBy(0, 200)")

# delete all
delete1 = driver.find_element(By.XPATH, "(//span[@title='Delete'])[1]")
delete1.click()
delete2 = driver.find_element(By.XPATH, "(//span[@title='Delete'])[1]")
delete2.click()
delete3 = driver.find_element(By.XPATH, "(//span[@title='Delete'])[1]")
delete3.click()

# add
time.sleep(1)
add = driver.find_element(By.XPATH, "//button[@id='addNewRecordButton']")
add.click()

time.sleep(1)
firstname = driver.find_element(By.XPATH, "//input[@id='firstName']")
firstname.clear()
firstname.send_keys("Ankit")

time.sleep(1)
lastname = driver.find_element(By.XPATH, "//input[@id='lastName']")
lastname.clear()
lastname.send_keys("Kumar")

time.sleep(1)
email = driver.find_element(By.XPATH, "//input[@id='userEmail']")
email.clear()
email.send_keys("ankit@gmail.com")

time.sleep(1)
age = driver.find_element(By.XPATH, "//input[@id='age']")
age.clear()
age.send_keys("22")

salary = driver.find_element(By.XPATH, "//input[@id='salary']")
salary.clear()
salary.send_keys("50000")

department = driver.find_element(By.XPATH, "//input[@placeholder='Department']")
department.clear()
department.send_keys("Computer Science & IT")

submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
submit_button.click()

# update
time.sleep(1)
edit_buttons = driver.find_elements(By.XPATH, "//span[@title='Edit']")
edit_buttons[-1].click()

time.sleep(1)
update_email = driver.find_element(By.XPATH, "//input[@placeholder='name@example.com']")
update_email.clear()
update_email.send_keys("kierra00000000002@example.com")

time.sleep(1)
submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
submit_button.click()

# keep browser open
time.sleep(9999)

# keep browser open
while True:
    pass

