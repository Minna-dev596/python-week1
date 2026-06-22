# 🔐 CLI Password Generator

## 📌 Project Description

This project is a Command Line Interface (CLI) based Password Generator and Strength Checker built using Python.
It allows users to generate secure passwords and evaluate their strength using predefined rules.

## ⚙️ Features

* Generate random secure passwords
* Customize password length and complexity
* Check password strength (Weak / Medium / Strong)
* Log all generated passwords into a file
* User-friendly CLI menu system

## 🛠️ Technologies Used

* Python 3
* Built-in libraries:

  * random
  * string
  * re (Regular Expressions)
  * datetime

## 🚀 How to Run the Project

### 1️⃣ Clone Repository (if using GitHub)
git clone <your-repo-link>
cd python-week1

### 2️⃣ Create Virtual Environment

python -m venv venv

### 3️⃣ Activate Virtual Environment

venv\Scripts\activate     # Windows
source venv/bin/activate  # Mac/Linux

### 4️⃣ Run the Program

python password_generator.py

## 📂 Output

* Generated passwords are saved in:

password_log.txt

## 🔎 Password Strength Criteria

* **Strong:** Minimum 8 characters, includes uppercase, lowercase, numbers, and symbols
* **Medium:** Minimum 6 characters
* **Weak:** Anything less than that

## 📌 Project Structure

python-week1/
│── password_generator.py
│── password_log.txt
│── README.md
│── requirements.txt

