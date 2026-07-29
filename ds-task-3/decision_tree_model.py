import sys
import os
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load Bank Marketing Dataset
dataset_path = os.path.join('data', 'bank_marketing.csv')
if not os.path.exists(dataset_path):
    print("Dataset not found. Generating Bank Marketing dataset...")
    import generate_bank_data

df = pd.read_csv(dataset_path)
print("==================================================")
print("🌳 Data Science Task 03: Decision Tree Classifier")
print("==================================================")
print(f"Dataset Shape: {df.shape}")
print(df.head())

# 2. Preprocess & Encode Categorical Variables
label_encoders = {}
df_encoded = df.copy()

categorical_cols = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'poutcome']
for col in categorical_cols:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col])
    label_encoders[col] = le

# Target Variable Encoding: 'yes' -> 1, 'no' -> 0
target_le = LabelEncoder()
df_encoded['deposit_subscribed'] = target_le.fit_transform(df_encoded['deposit_subscribed'])

X = df_encoded.drop(columns=['deposit_subscribed'])
y = df_encoded['deposit_subscribed']

# 3. Train-Test Split (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 4. Train Decision Tree Classifier with Pruning (max_depth=5)
dt_model = DecisionTreeClassifier(criterion='entropy', max_depth=5, min_samples_split=10, random_state=42)
dt_model.fit(X_train, y_train)

# 5. Model Evaluation
y_pred = dt_model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("\n📈 Decision Tree Performance Evaluation:")
print(f"   • Overall Accuracy: {acc * 100:.2f}%")

print("\n📋 Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(f"   [[ TN (No/No): {cm[0][0]} | FP (No/Yes): {cm[0][1]} ]")
print(f"    [ FN (Yes/No): {cm[1][0]} | TP (Yes/Yes): {cm[1][1]} ]]")

print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred, target_names=['No Subscription (0)', 'Subscribed (1)']))

# 6. Feature Importance Breakdown
print("\n🔍 Top Decision Factors (Feature Importance):")
importances = pd.Series(dt_model.feature_importances_, index=X.columns).sort_values(ascending=False)
for col, imp in importances.items():
    print(f"   • {col:15s}: {imp * 100:.2f}%")

# 7. Save Model & Encoders
os.makedirs('models', exist_ok=True)
model_path = os.path.join('models', 'bank_tree_model.pkl')
encoders_path = os.path.join('models', 'label_encoders.pkl')

with open(model_path, 'wb') as f:
    pickle.dump(dt_model, f)
with open(encoders_path, 'wb') as f:
    pickle.dump(label_encoders, f)

print(f"\n[OK] Decision Tree model saved to '{model_path}'")
