# 📚 Auto Question Generator

A Flask-based web application that automatically generates and serves questions from a CSV file based on user-selected **topic** and **difficulty level**. Ideal for assessment platforms, coding practice tools, and educational apps.

---

## 🚀 Features

- 🔍 Load and filter questions based on:
  - **Topic**: Arrays, Linked Lists, Trees
  - **Difficulty**: 1 (Easy), 2 (Intermediate), 3 (Advance)
- 🔄 Randomized question selection
- ✅ View questions and answers via frontend
- 📁 CSV-based question storage (easy to update)
- 🧩 Modular code design for easy extension

---

## 🧰 Tech Stack

- **Backend**: Python 3.11, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Data Handling**: Pandas
- **Storage**: CSV file (`data/questions.csv`)
- **Randomization** : Random 

---

## 📂 Project Structure

```text
Auto-Question-Generator/
│
├── data/
│   └── questions.csv          # Question bank (id, topic, difficulty, question, answer)
│
├── static/                    # Static assets (CSS/JS)
├── templates/                 # HTML templates
│   ├── index.html             # Main UI
│   └── base.html              # Shared layout
│
├── utils/                     # Utility functions 
├── tests/                     # Test cases 
│
├── app.py                     # Main Flask app
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

---
```
## 📦 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/indrajeet-77/Auto-Question-Generator-Akshara-Plus-Org-.git
cd Auto-Question-Generator
2. Create Virtual Environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the App
bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000/ in your browser.

## ⚙️ Core Functions
load_questions(): Reads question data from CSV file.

filter_questions(topic, difficulty, num_questions): Filters and samples questions based on user input.

## 📌 Contribution
Feel free to fork the repo, raise issues, or submit pull requests. Suggestions and improvements are welcome!

## 🧑‍💻 Author
- Indrajeet Pimpalgaonkar
- Vedant Patil
- Sayali Munde




> 
