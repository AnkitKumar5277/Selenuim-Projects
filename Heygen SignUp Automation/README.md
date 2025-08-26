# Heygen AutoSign 🚀

Automated script for creating a **Heygen account** using **Selenium** and **Temp Mail**.
The script automatically:

1. Fetches a temporary email from [Temp-Mail](https://temp-mail.org/)
2. Uses it to sign up on [Heygen](https://app.heygen.com/login)
3. Extracts the verification code from the email
4. Completes the account creation flow with auto-generated password
5. Selects the free plan and sets up initial onboarding

---

## ⚙️ Features

* Automated **temporary email generation**
* **Heygen account registration** without manual effort
* Auto-handling of **verification code**
* Creates a **password** using email
* Auto-selects onboarding options (`Free → Personal → Hobbyist → Fun Project`)
* Keeps the browser open after execution for further use

---

## 📦 Requirements

Make sure you have the following installed:

* Python **3.8+**
* Microsoft Edge Browser
* [Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) (same version as your browser)
* Required Python packages:

  ```bash
  pip install selenium pyperclip
  ```

---

## ▶️ How to Run

1. Clone this repository or copy the script.
2. Ensure **Edge WebDriver** is in your system PATH.
3. Run the script:

   ```bash
   python heygen_automate_login.py
   ```
4. The script will:

   * Open Temp-Mail → copy temp email
   * Open Heygen → sign up with the email
   * Auto-verify using received code
   * Complete the signup & onboarding

---

## 📝 Code Overview

* **Step 1**: Open Temp-Mail and copy email to clipboard
* **Step 2**: Open Heygen signup page
* **Step 3**: Enter email & wait for verification mail
* **Step 4**: Extract verification code & paste in Heygen
* **Step 5**: Set password, accept terms, create account
* **Step 6**: Select `Free Plan → Personal → Hobbyist → Fun Project`

---

## ⚠️ Notes

* This script is for **educational purposes only**.
* Heygen may update their UI, so you might need to adjust XPath/CSS selectors.
* Running too frequently may get flagged by Heygen.

---

## ✅ Example Output

```bash
Temporary Email: qwerty123@some-temp-mail.org
Switched back to Temp Mail tab.
Copied verification code to clipboard: 547891
✅ Verification process completed! Browser will remain open.
```

---

## 📌 Author

👨‍💻 Developed by **ANKIT KUMAR**
📧 Contact: ankitx66@gmail.com
