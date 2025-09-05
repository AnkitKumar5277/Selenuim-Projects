Here’s a simple **README.md** for your Selenium parallel execution script:

---

# 🧪 Parallel Selenium Test Script

This project demonstrates how to run a Selenium automation test in **multiple browsers (Edge & Chrome) simultaneously** using **Python threading**.

The script:

1. Opens the **Applitools Demo Banking site**.
2. Logs in with demo credentials.
3. Extracts all **transaction amounts** from the web table.
4. Cleans and converts them into numeric values (including negative numbers).
5. Calculates the **total sum**.
6. Runs in **Edge and Chrome in parallel**.

---

## 🚀 Tech Stack

* **Python 3**
* **Selenium WebDriver**
* **Threading (for parallel execution)**

---

## 📂 Project Structure

```
parallel-selenium-test/
│── main.py          # The main script with parallel execution
│── README.md        # Documentation
```

---

## ⚙️ Installation & Setup

1️⃣ Install dependencies:

```bash
pip install selenium webdriver-manager
```

2️⃣ Download & install **browsers** (Chrome, Edge).

3️⃣ Run the script:

```bash
python main.py
```

---

## 🖥️ Output Example

When you run the script, it will:

* Launch **Edge** and **Chrome** simultaneously.
* Extract numbers from the table.
* Print the results per browser.

Example output:

```
🌐 Browser: EDGE
Extracted values: [1250.0, -320.0, 850.0, 200.0]
✅ Total Sum = 1980.0
🚀 Test finished in EDGE

🌐 Browser: CHROME
Extracted values: [1250.0, -320.0, 850.0, 200.0]
✅ Total Sum = 1980.0
🚀 Test finished in CHROME

🎉 Both browsers completed successfully!
```

---

## 🧾 Notes

* The script uses **threading** → Edge and Chrome run **in parallel**.
* Works with **dynamic values** (handles positive and negative numbers).
* Uses `.quit()` at the end to close browsers automatically.

---

Do you want me to also include **step-by-step screenshots** of execution (login, table extraction, etc.) inside the README? That will make it more beginner-friendly.
