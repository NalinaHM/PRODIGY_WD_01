import os

files = [
    r'c:\prodig\ml-task-1\generate_dataset.py',
    r'c:\prodig\ml-task-1\model.py',
    r'c:\prodig\ml-task-1\predict.py',
    r'c:\prodig\ml-task-2\generate_dataset.py',
    r'c:\prodig\ml-task-2\cluster_model.py',
    r'c:\prodig\ml-task-3\synthetic_images.py',
    r'c:\prodig\ml-task-3\train_svm.py',
    r'c:\prodig\ml-task-4\generate_gestures.py',
    r'c:\prodig\ml-task-4\train_gesture_model.py',
    r'c:\prodig\ml-task-5\food_dataset.py',
    r'c:\prodig\ml-task-5\train_food_model.py'
]

header = "import sys\nsys.stdout.reconfigure(encoding='utf-8')\n"

for path in files:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        if "reconfigure(encoding='utf-8')" not in content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(header + content)
            print(f"Updated {path}")

print("Fixed stdout encodings in all ML python scripts.")
