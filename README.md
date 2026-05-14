A Machine Learning based web application that predicts the possibility of diabetes using health parameters such as Age, BMI, Fasting Sugar, HbA1c, Gender, Hypertension, and Family History.

The application is built using Python, Flask, HTML/CSS, and Machine Learning.

---

# Features

* Diabetes prediction using ML model
* User-friendly web interface
* Real-time prediction results
* Input validation
* Simple and responsive UI

---

# Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* HTML
* CSS

---

# Project Structure

```bash
Diabetes-Prediction-App/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── model/
│   └── diabetes_model.pkl
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── dataset.csv
```

---

# Input Parameters

* Age
* BMI
* Fasting Sugar
* HbA1c
* Gender
* Hypertension
* Family History of Diabetes

---

# Sample Frontend Form

```html
Age:
BMI:
Fasting Sugar:
HBA1C:
Gender: Female Male
Hypertension: No Yes
Family History of Diabetes: No Yes
Predict

{% if result %}
Result: {{ result }}
{% endif %}
```

---

# Installation

```bash
git clone https://github.com/piyushdoke1/diabetes-prediction-app.git
cd diabetes-prediction-app
pip install -r requirements.txt
python app.py
```

---

# Requirements

flask
pandas
numpy
scikit-learn
joblib

---

# Run the Project

```bash
python app.py
```

Then open:

```bash
http://127.0.0.1:5000/
```

---

# Example README for GitHub

```md
# Diabetes Prediction App

A Machine Learning based web application that predicts diabetes using health-related parameters.

## Features
- Predicts diabetes risk
- Flask web application
- ML-powered predictions
- Responsive UI

## Tech Stack
Python, Flask, Scikit-learn, HTML, CSS

## Installation
pip install -r requirements.txt
python app.py
```

---

# Suggested GitHub Topics

* machine-learning
* flask
* diabetes-prediction
* healthcare-ai
* python-project
* ml-web-app

---

# Suggested Commit Message

```bash
Initial commit - Diabetes Prediction ML Web App
```
