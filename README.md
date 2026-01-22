# 🏠 House Price Prediction

## 📌 Project Overview
This project predicts house prices using **Machine Learning (Linear Regression)**.
The **California Housing Dataset** from scikit-learn is used.

## 📊 Dataset
- Source: `sklearn.datasets.fetch_california_housing`
- Rows: 20,640
- Features: 8
- Target: Median House Value

## 🛠 Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## 🔄 ML Workflow
1. Data Loading
2. Exploratory Data Analysis
3. Train-Test Split
4. Model Training (Linear Regression)
5. Model Evaluation (RMSE, R²)
6. Model Saving using Joblib

## 📈 Results
- RMSE ≈ 0.74  
- R² Score ≈ 0.57  

## ▶️ How to Run

```bash

pip install -r requirements.txt
python predict.py
💾 Saved Model
house_price_model.pkl

The trained model is saved as:

house_price_model.pkl
⚠️ Note: The `.pkl` file is a binary ML model and cannot be viewed directly on GitHub.



