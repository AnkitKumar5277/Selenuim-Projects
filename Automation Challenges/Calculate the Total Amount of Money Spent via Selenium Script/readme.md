This project demonstrates how to run a Selenium automation test in **multiple browsers (Edge & Chrome) simultaneously** using **Python threading**.

The script:

1. Opens the **Applitools Demo Banking site**.
2. Logs in with demo credentials.
3. Extracts all **transaction amounts** from the web table.
4. Cleans and converts them into numeric values (including negative numbers).
5. Calculates the **total sum**.
6. Runs in **Edge and Chrome in parallel**.

## 🧾 Notes

* The script uses **threading** → Edge and Chrome run **in parallel**.
* Works with **dynamic values** (handles positive and negative numbers).
* Uses `.quit()` at the end to close browsers automatically.

<img width="1920" height="1050" alt="Screenshot 2026-01-21 002837" src="https://github.com/user-attachments/assets/1031e85a-8f1a-4f3c-8902-ce92371c17d1" />

<img width="1920" height="1050" alt="Screenshot 2026-01-21 002848" src="https://github.com/user-attachments/assets/624f46ac-3b92-429f-832b-4d652d65015e" />

<img width="1920" height="1050" alt="Screenshot 2026-01-21 002944" src="https://github.com/user-attachments/assets/a1548fed-9b83-4b44-99ac-b191f1ff0684" />
