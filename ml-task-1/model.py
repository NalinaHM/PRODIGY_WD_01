import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1. Load Data
dataset_path = os.path.join('data', 'house_prices.csv')
if not os.path.exists(dataset_path):
    print("Dataset not found. Running dataset generator...")
    import generate_dataset

df = pd.read_csv(dataset_path)
print(f"📊 Dataset Shape: {df.shape}")
print(df.head())

# 2. Features and Target Variable
X = df[['square_feet', 'bedrooms', 'bathrooms', 'age_years', 'garage_spaces']]
y = df['price']

# 3. Train-Test Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate Model
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n📈 Model Performance Evaluation:")
print(f"   • Mean Absolute Error (MAE):  ${mae:,.2f}")
print(f"   • Root Mean Squared Error (RMSE): ${rmse:,.2f}")
print(f"   • R² Score (Variance Explained): {r2:.4f} ({r2*100:.2f}%)")

print("\n🔍 Linear Regression Coefficients:")
for col, coef in zip(X.columns, model.coef_):
    print(f"   • {col}: ${coef:,.2f} per unit")
print(f"   • Intercept: ${model.intercept_:,.2f}")

# 6. Save Trained Model
os.makedirs('models', exist_ok=True)
model_path = os.path.join('models', 'linear_regression_model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"\n💾 Model successfully saved to '{model_path}'")
