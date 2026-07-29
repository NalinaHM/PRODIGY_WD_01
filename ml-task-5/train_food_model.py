import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score

# 1. Load Food Dataset
dataset_path = os.path.join('data', 'food_items.csv')
if not os.path.exists(dataset_path):
    print("Dataset not found. Generating sample food items...")
    import food_dataset

df = pd.read_csv(dataset_path)
print(f"📊 Dataset Shape: {df.shape}")

X = df[['red_ratio', 'green_ratio', 'blue_ratio', 'texture_smoothness', 'density_est']]
y_class = df['food_label']
y_cal = df['calories_100g']

# 2. Train-Test Split (80/20)
X_train, X_test, y_class_train, y_class_test, y_cal_train, y_cal_test = train_test_split(
    X, y_class, y_cal, test_size=0.2, random_state=42, stratify=y_class
)

# 3. Train Food Recognition Classifier
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_class_train)

# 4. Train Calorie Estimation Regressor
regressor = GradientBoostingRegressor(n_estimators=100, random_state=42)
regressor.fit(X_train, y_cal_train)

# 5. Evaluate Models
class_pred = classifier.predict(X_test)
cal_pred = regressor.predict(X_test)

class_acc = accuracy_score(y_class_test, class_pred)
cal_mae = mean_absolute_error(y_cal_test, cal_pred)
cal_r2 = r2_score(y_cal_test, cal_pred)

print("\n🍕 Food Recognition & Calorie Estimator Evaluation:")
print(f"   • Food Classification Accuracy: {class_acc * 100:.2f}%")
print(f"   • Calorie Estimation MAE:        {cal_mae:.2f} kcal / 100g")
print(f"   • Calorie Estimation R² Score:   {cal_r2:.4f}")

# 6. Save Models
os.makedirs('models', exist_ok=True)
with open(os.path.join('models', 'food_classifier.pkl'), 'wb') as f:
    pickle.dump(classifier, f)
with open(os.path.join('models', 'calorie_regressor.pkl'), 'wb') as f:
    pickle.dump(regressor, f)

print("💾 Trained Food Recognition & Calorie Estimation models exported to 'models/'")
