# 💰 Salary Prediction Using Machine Learning

## 📌 Project Overview

This project predicts employee salaries based on professional attributes such as experience, skills score, and education level.

The goal is to estimate salary using Machine Learning and provide an interactive web application where users can enter their details and receive a salary prediction instantly.

🌐 Live Demo: [(https://marks-prediction-app-1.streamlit.app/)]

---

## 🛠 Technologies Used

- Python
- Pandas
- Scikit-Learn
- Streamlit
- Joblib

---

## 📊 Features Used

### Input Features

- Experience (Years)
- Skills Score (1–10)
- Education Level

### Target Variable

- Salary

---

## 🧹 Data Preprocessing

- Dataset Cleaning
- Feature Selection
- Train-Test Split

---

## 🤖 Models Evaluated

The following regression approaches were tested:

1. Linear Regression
2. Polynomial Features
3. Ridge Regression

### Model Comparison (MAE)

| Model | Mean Absolute Error |
|---------|---------|
| Linear Regression | 1449 |
| Polynomial Features | 1250 |
| Ridge Regression | 995 |

---

## ✅ Final Model Selection

**Ridge Regression** was selected because it achieved the lowest prediction error and provided the most reliable performance.

---

## 🚀 Application Features

- Interactive Streamlit UI
- Experience-based Salary Prediction
- Education Level Selection
- Skills Score Evaluation
- Real-time Salary Estimation

---

## 📂 Project Structure

```text
Salary-Prediction-ML/
│
├── salary.csv
├── salary_model.pkl
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
```

---

## 🌐 Live Demo

[(https://marks-prediction-app-1.streamlit.app/)]

---

## 👨‍💻 Author

**Abhishek Pal**
