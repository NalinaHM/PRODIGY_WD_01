import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 1. Load Image Features
dataset_path = os.path.join('data', 'dogs_vs_cats_features.csv')
if not os.path.exists(dataset_path):
    print("Dataset not found. Generating features...")
    import synthetic_images

df = pd.read_csv(dataset_path)
print(f"📊 Dataset Shape: {df.shape}")

X = df.drop(columns=['label'])
y = df['label']

# 2. Train-Test Split (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 3. Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Train Support Vector Machine (SVM) Model
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale', probability=True, random_state=42)
svm_model.fit(X_train_scaled, y_train)

# 5. Evaluate Model
y_pred = svm_model.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)

print("\n🐶🐱 Support Vector Machine (SVM) Classification Results:")
print(f"   • Test Accuracy: {acc * 100:.2f}%")
print("\n📋 Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(f"   [[ TN (Cat as Cat): {cm[0][0]} | FP (Cat as Dog): {cm[0][1]} ]")
print(f"    [ FN (Dog as Cat): {cm[1][0]} | TP (Dog as Dog): {cm[1][1]} ]]")

print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Cat (0)', 'Dog (1)']))

# 6. Save Scaler & SVM Model
os.makedirs('models', exist_ok=True)
model_path = os.path.join('models', 'dog_cat_svm_model.pkl')
scaler_path = os.path.join('models', 'scaler.pkl')

with open(model_path, 'wb') as f:
    pickle.dump(svm_model, f)
with open(scaler_path, 'wb') as f:
    pickle.dump(scaler, f)

print(f"💾 Trained SVM Model & Scaler exported to '{model_path}'")
