CURA Healthcare Appointment Automation 🧠

This project automates the process of booking an appointment on the CURA Healthcare Service demo website using Selenium WebDriver in Microsoft Edge (InPrivate) mode.

🔧 Requirements

Python 3.9 or above

Selenium 4+

Microsoft Edge (latest version)

Edge WebDriver (auto-managed by Selenium 4.6+)

Optional:

PyTest → for running as a test

Allure → for HTML reporting

📦 Install Dependencies

Create a virtual environment and install the packages:

python -m venv .venv
.venv\Scripts\activate        # On Windows
pip install selenium pytest allure-pytest

▶️ How to Run
Option 1 — Run directly
python main.py

Option 2 — Run with PyTest and generate report
pytest -s main.py --alluredir=reports
allure serve reports

🧰 What the Script Does

Opens https://katalon-demo-cura.herokuapp.com/

Clicks Make Appointment

Logs in using:

Username: John Doe

Password: ThisIsNotAPassword

Fills appointment details:

Facility: Hongkong CURA Healthcare Center

Program: Medicaid

Visit Date: 30th

Comment: “This is an automated appointment request.”

Books the appointment

Prints:

Appointment successfully booked! Browser will close in 10 seconds.

🧾 Project Structure
.
├── main.py
├── README.md
└── reports/   # (auto-created for Allure reports)

✅ Notes

Make sure Edge browser is up to date.

Selenium 4.6+ automatically manages WebDriver — no manual driver setup needed.

You can increase wait times if elements load slowly.

📜 License

Free to use for learning and testing purposes.
