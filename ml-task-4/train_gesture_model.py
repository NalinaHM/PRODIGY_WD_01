import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 1. Load Hand Gesture Features
dataset_path = os.path.join('data', 'hand_gestures.csv')
if not os.path.exists(dataset_path):
    print("Dataset not found. Generating gesture samples...")
    import generate_gestures

df = pd.read_csv(dataset_path)
print(f"📊 Dataset Shape: {df.shape}")

X = df.drop(columns=['gesture_id'])
y = df['gesture_id']

gesture_map = {0: 'Open Palm 🖐️', 1: 'Closed Fist ✊', 2: 'Peace Sign ✌️', 3: 'Thumbs Up 👍', 4: 'OK Sign 👌'}

# 2. Train-Test Split (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 3. Train Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
rf_model.fit(X_train, y_train)

# 4. Evaluate Model
y_pred = rf_model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("\n🖐️ Hand Gesture Recognition Model Evaluation:")
print(f"   • Overall Accuracy: {acc * 100:.2f}%")
print("\n📊 Classification Report:")
target_names = [gesture_map[i] for i in range(5)]
print(classification_report(y_test, y_pred, target_names=target_names))

# 5. Save Model
os.makedirs('models', exist_ok=True)
model_path = os.path.join('models', 'gesture_rf_model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(rf_model, f)

print(f"💾 Gesture Classifier Model exported to '{model_path}'")
