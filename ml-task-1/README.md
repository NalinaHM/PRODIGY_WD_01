# Prodigy InfoTech Machine Learning Track - Task 01
## House Price Prediction using Linear Regression

### 📌 Overview
Implement a Linear Regression model to predict house prices based on key features such as square footage, bedrooms, bathrooms, house age, and garage capacity.

### 🛠️ Architecture & Workflow
1. **Dataset Generation / Ingestion**: `generate_dataset.py` generates sample real estate records saved to `data/house_prices.csv`.
2. **Model Training & Evaluation**: `model.py` splits data (80% train / 20% test), fits a `LinearRegression` estimator, computes performance metrics (MAE, RMSE, $R^2$ Score), and exports `models/linear_regression_model.pkl`.
3. **Interactive Inference**: `predict.py` takes user parameters and outputs instant price estimates.

### 🚀 How to Run

```bash
# 1. Generate Dataset & Train Model
python model.py

# 2. Run Interactive Predictor
python predict.py
```

### 📊 Model Metrics Sample
- **Mean Absolute Error (MAE)**: ~$9,500
- **Root Mean Squared Error (RMSE)**: ~$12,100
- **$R^2$ Score**: ~0.985 (98.5% Variance Explained)
