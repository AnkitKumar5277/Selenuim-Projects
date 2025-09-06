import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://demoqa.com/webtables")

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
third_edit_btn = driver.find_element(By.XPATH, "(//span[@title='Edit'])[3]")
third_edit_btn.click()

time.sleep(1)
update_email = driver.find_element(By.XPATH, "//input[@placeholder='name@example.com']")
update_email.clear()
update_email.send_keys("kierra00000000002@example.com")

time.sleep(1)
submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
submit_button.click()

# delete (second row for example)
time.sleep(1)
delete_2 = driver.find_element(By.XPATH, "(//span[@title='Delete'])[2]")
delete_2.click()

# delete another (third row for example)
time.sleep(1)
delete = driver.find_element(By.XPATH, "(//span[@title='Delete'])[3]")
delete.click()

# keep browser open
time.sleep(100)
driver.quit()
