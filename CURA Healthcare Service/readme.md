# CURA Healthcare Appointment Automation 🧠

This project automates the process of booking an appointment on the **CURA Healthcare Service** demo website using **Selenium WebDriver** in **Microsoft Edge (InPrivate)** mode.

---

## 🔧 Requirements

* Python 3.9 or above
* Selenium 4+
* Microsoft Edge (latest version)
* Edge WebDriver (auto-managed by Selenium 4.6+)
* Optional:

  * **PyTest** → for running as a test
  * **Allure** → for HTML reporting

---

## 📦 Install Dependencies

Create a virtual environment and install the packages:

```bash
python -m venv .venv
.venv\Scripts\activate        # On Windows
pip install selenium pytest allure-pytest
```

---

## ▶️ How to Run

### Option 1 — Run directly

```bash
python main.py
```

### Option 2 — Run with PyTest and generate report

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

---

## 🧾 Project Structure

```
.
├── main.py
├── README.md
└── reports/   # (auto-created for Allure reports)
```

---

## ✅ Notes

* Make sure Edge browser is up to date.
* Selenium 4.6+ automatically manages WebDriver — no manual driver setup needed.
* You can increase wait times if elements load slowly.

---

## 📜 License

Free to use for learning and testing purposes.
