# Customer_Retention_Analytics_and_Churn_Prediction_System

An end-to-end Machine Learning project that predicts customer churn using classification algorithms and deploys real-time predictions through a Streamlit web application.

---

# Project Overview

Customer churn prediction is a critical business problem that helps organizations identify customers who are likely to discontinue services.

This project implements:
- Data preprocessing pipelines
- Exploratory Data Analysis (EDA)
- Feature engineering
- Multiple ML model comparison
- Ensemble learning
- Real-time prediction deployment

The final model was deployed using Streamlit for interactive churn prediction.

---

# Features

- Automated preprocessing using Scikit-learn Pipelines
- OneHotEncoding for categorical variables
- Feature scaling using StandardScaler
- Multiple model training and evaluation
- Model comparison workflow
- Feature importance analysis
- Real-time churn prediction web app
- Deployment-ready architecture

---

# Tech Stack

## Programming Language
- Python

## Libraries & Frameworks
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

# Machine Learning Models Used

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)

---

# Model Performance

|      Model          | Accuracy|
|---------------------|---------|
| Logistic Regression |  82.9%  |
| Decision Tree       |  95.9%  |
| Random Forest       |  96.8%  |
| K Nearest Neighbor  |  89.8%  |

Random Forest achieved the best overall performance and was selected as the final production model.

---

# Project Workflow

```text
Data Collection
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Preprocessing Pipeline
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Feature Importance Analysis
      ↓
Model Serialization
      ↓
Streamlit Deployment
```

---

# Dataset Features

- Age
- Gender
- Tenure
- Usage Frequency
- Support Calls
- Payment Delay
- Subscription Type
- Contract Length
- Total Spend
- Last Interaction

Target Variable:
- Churn (0 = Stay, 1 = Churn)

---

# Project Structure

```text
Customer-Churn-Prediction/
│
├── app.py
├── churn_pipeline.pkl
├── requirements.txt
├── code_file.ipynb
├── customer_churn_dataset-testing-master.csv
└── README.md
```

---
