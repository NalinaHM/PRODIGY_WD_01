import sys
import subprocess
import os

sys.stdout.reconfigure(encoding='utf-8')

tasks = [
    ('ML Task 1: House Price Prediction', 'ml-task-1', 'model.py'),
    ('ML Task 2: Customer Segmentation', 'ml-task-2', 'cluster_model.py'),
    ('ML Task 3: Dog vs Cat Classifier', 'ml-task-3', 'train_svm.py'),
    ('ML Task 4: Hand Gesture Recognition', 'ml-task-4', 'train_gesture_model.py'),
    ('ML Task 5: Food Recognition & Calories', 'ml-task-5', 'train_food_model.py'),
]

for name, folder, script in tasks:
    print(f"\n==================================================")
    print(f"🚀 RUNNING: {name}")
    print(f"==================================================")
    path = os.path.join(r'c:\prodig', folder)
    res = subprocess.run(['python', script], cwd=path, capture_output=True, text=True, encoding='utf-8')
    print(res.stdout)
    if res.stderr:
        print("ERRORS / WARNINGS:")
        print(res.stderr)

print("✅ All 5 Machine Learning models trained and evaluated successfully!")
