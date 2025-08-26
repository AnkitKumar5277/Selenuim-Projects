from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip

# Step 1: Set Edge options (Incognito + Keep browser open after script ends)
options = webdriver.EdgeOptions()
  # Enable incognito mode
options.add_experimental_option("detach", True)  # Keep browser open

# Step 2: Launch Edge
driver = webdriver.Edge(options=options)
wait = WebDriverWait(driver, 20)

# Step 3: Open Temp Mail
driver.get("https://temp-mail.org/en/")

# Wait for Copy button and click
copy_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='click-to-copy']")))
copy_button.click()
time.sleep(1)

# Get email from Clipboard
email_address = pyperclip.paste().strip()
print("Temporary Email:", email_address)

# Step 4: Open Heygen in NEW TAB
driver.execute_script("window.open('https://app.heygen.com/login','_blank');")
driver.switch_to.window(driver.window_handles[1])
wait2 = WebDriverWait(driver, 20)

# Click Sign Up
sign_up_button = wait2.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Sign Up')]")))
sign_up_button.click()

time.sleep(2)
# Enter Email
email_input = wait2.until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))
email_input.send_keys(email_address)

# Click Send
send_button = wait2.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-7orpxh.btnContent")))
send_button.click()
time.sleep(2)
# Switch back to Temp Mail tab
driver.switch_to.window(driver.window_handles[0])
print("Switched back to Temp Mail tab.")

# Wait for verification email (can take a while)

recieved = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='viewLink title-subject nu-reward'])[2]")))
recieved.click()

# Extract verification code
element = wait.until(EC.presence_of_element_located((By.XPATH, "//strong[@style='box-sizing: border-box;']")))
number = element.text.strip()
pyperclip.copy(number)
print(f"Copied verification code to clipboard: {number}")

# Switch back to Heygen tab
driver.switch_to.window(driver.window_handles[1])

# Enter verification code
verify_input = wait2.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@class,'css-1q82o10')]")))
verify_input.send_keys(number)

# Click Verify
verify_button = wait2.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Verify']")))
verify_button.click()

# Wait for email text element (on Heygen page)
email_el = wait2.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.css-xrdlog")))
email_text = email_el.text.strip()

# Add 'H' at start (use as password)
modified_email = "H" + email_text
pyperclip.copy(modified_email)

# Fill password and confirm password
wait3 = WebDriverWait(driver, 20)
fill_password = wait3.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']")))
fill_password.send_keys(modified_email)

confirm_password = wait3.until(EC.presence_of_element_located((By.XPATH, "//input[@id='pwdConfirm']")))
confirm_password.send_keys(modified_email)

# Tick checkbox
checkbox = driver.find_element(By.XPATH, "//input[@class='css-80mtdc' and @type='checkbox']")
checkbox.click()

# Click Create Account
element = driver.find_element(By.XPATH, "//span[text()='Create Account']")
element.click()

wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Choose Free']")))
button.click()

wait = WebDriverWait(driver, 10)
personal_div = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Personal']")))
personal_div.click()

wait = WebDriverWait(driver, 10)
continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Continue']")))
continue_btn.click()

wait = WebDriverWait(driver, 10)
hobbyist_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Hobbyist']")))
hobbyist_btn.click()

wait = WebDriverWait(driver, 10)
continue_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Continue']"))
)
continue_btn.click()

wait = WebDriverWait(driver, 10)
project_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='A fun and creative project']"))
)
# Click the element
project_btn.click()

wait = WebDriverWait(driver, 10)
submit_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
)

# Click the button
submit_btn.click()

print("✅ Verification process completed! Browser will remain open.")
