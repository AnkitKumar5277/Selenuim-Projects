# CURA Healthcare Appointment Automation 🧠

This project automates the process of booking an appointment on the **CURA Healthcare Service** demo website using **Selenium WebDriver** in **Microsoft Edge (InPrivate)** mode.

---

## 🔧 Requirements

* Python 3.9 or above
* Selenium 4+
* Optional:
  * **PyTest** → for running as a test
  * **Allure** → for HTML reporting

---

## 📦 Install Dependencies

---

## ▶️ How to Run

```

### Run with PyTest and generate report

```bash
pytest -s main.py --alluredir=reports
allure serve reports
```

---

## 🧰 What the Script Does

1. Opens `https://katalon-demo-cura.herokuapp.com/`
2. Clicks **Make Appointment**
3. Logs in using:

   * Username: `John Doe`
   * Password: `ThisIsNotAPassword`
4. Fills appointment details:
   * Facility: *Hongkong CURA Healthcare Center*
   * Program: *Medicaid*
   * Visit Date: *30th*
   * Comment: *“This is an automated appointment request.”*
5. Books the appointment
6. Prints:

   ```
   Appointment successfully booked! Browser will close in 10 seconds.
   ```
