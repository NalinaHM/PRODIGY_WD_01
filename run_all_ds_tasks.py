import sys
import subprocess
import os

sys.stdout.reconfigure(encoding='utf-8')

tasks = [
    ('DS Task 1: Demographic Distribution Analysis', 'ds-task-1', 'analyze_visualize.py'),
    ('DS Task 2: Titanic Data Cleaning & EDA', 'ds-task-2', 'clean_and_eda.py'),
    ('DS Task 3: Bank Marketing Decision Tree', 'ds-task-3', 'decision_tree_model.py'),
    ('DS Task 4: Social Media Sentiment Analysis', 'ds-task-4', 'sentiment_analysis.py'),
    ('DS Task 5: Traffic Accident Hotspot Analysis', 'ds-task-5', 'accident_analysis.py'),
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

print("✅ All 5 Data Science tasks executed successfully!")
