# Opencart Registration Account Testing With Selenium (Mini Project 3)

## Overview
This project automates the registration process on the Opencart demo site using Selenium, Pytest, and Allure Reports.  
It verifies that a user can successfully register an account with valid data.

## Tools and Technologies
- Python
- Selenium WebDriver
- Pytest
- Allure Reports
- Microsoft Edge Browser

## Test Case Details
**Test Name:** test_awesome_qa  
**Test Type:** Positive Test Case  
**Description:** Fill the registration form with valid data and verify account creation.

## Prerequisites
1. Install Python 3.x  
2. Install dependencies:
   ```bash
   pip install selenium pytest allure-pytest

3. Install Edge WebDriver and ensure it matches your Edge browser version.

## How to Run

1. Run the test:

   ```bash
   pytest -s main.py --alluredir=reports
   ```
2. Generate and view Allure report:

   ```bash
   allure serve reports
   ```

## Expected Result

* Registration completes successfully.
* Success message displayed: **"Your Account Has Been Created!"**
* URL after success:

  ```
  https://awesomeqa.com/ui/index.php?route=account/success
  ```

## Project Structure

```
selenium_opencart_project/
│
├── main.py         # Main test script
├── reports/        # Allure reports
└── README.md       # Project info
```
<img width="1920" height="1050" alt="Screenshot 2026-01-22 204103" src="https://github.com/user-attachments/assets/9251bdc2-8f90-4bee-8e56-665ad306f602" />

<img width="1920" height="1050" alt="Screenshot 2026-01-22 204138" src="https://github.com/user-attachments/assets/8e015c4b-63dc-416d-8139-c8d7cf2459fc" />



