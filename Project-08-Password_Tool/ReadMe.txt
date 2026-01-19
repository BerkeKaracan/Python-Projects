# 🔐 Password Security Toolkit

A Python-based CLI (Command Line Interface) tool designed to analyze password strength and generate cryptographically strong passwords. This project demonstrates logical algorithm design, string manipulation, and robust error handling.

## 🚀 Features

* **Algorithmic Scoring System:** Evaluates passwords based on length, case sensitivity, digits, and special characters.
* **Detailed Feedback:** Provides specific recommendations on how to improve weak passwords (e.g., "Missing a special character").
* **Smart Generator:** Creates strong passwords using a secure loop mechanism that ensures the output meets high-security standards.
* **Dynamic Logic:** Automatically adjusts difficulty thresholds for shorter custom lengths to prevent infinite loops.
* **Error Handling:** Robust input validation (`try-except`) prevents crashes from invalid user inputs.

## 🛠️ Built With

* **Python 3.13
* **Libraries: `random`, `string`

## 💻 How to Run

1.  Clone the repository:
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/REPO_ADIN.git](https://github.com/BerkeKaracan/Python-Projects.git)
    ```
2.  Navigate to the directory:
    ```bash
    cd Python-Projects
    ```
3.  Run the script:
    ```bash
    python password_tool.py
    ```

## 🧠 Code Highlights

This project focuses on **backend logic**:

* **Modular Functions:** Separated logic for `scorer()` (analysis) and `password_tool()` (generation).
* **Infinite Loop Prevention:** The generator resets variables inside the loop scope to ensure fresh attempts every iteration.
* **User Experience (UX):** Clean CLI menu with clear instructions and feedback.