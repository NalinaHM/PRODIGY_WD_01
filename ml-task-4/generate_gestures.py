import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import random
import csv
import numpy as np

os.makedirs('data', exist_ok=True)
filepath = os.path.join('data', 'hand_gestures.csv')

# 5 Hand Gestures for Human-Computer Interaction (HCI):
# 0: Open Palm, 1: Closed Fist, 2: Peace / V-Sign, 3: Thumbs Up, 4: OK Sign
gesture_labels = {0: 'Open Palm', 1: 'Closed Fist', 2: 'Peace Sign', 3: 'Thumbs Up', 4: 'OK Sign'}

headers = ['thumb_ext', 'index_ext', 'middle_ext', 'ring_ext', 'pinky_ext', 'gesture_id']

random.seed(42)
np.random.seed(42)

rows = []
for gesture_id in range(5):
    for _ in range(250):  # 250 samples per gesture class
        if gesture_id == 0:   # Open Palm: all fingers extended (~1.0)
            t = np.random.normal(0.95, 0.05)
            i = np.random.normal(0.95, 0.05)
            m = np.random.normal(0.95, 0.05)
            r = np.random.normal(0.95, 0.05)
            p = np.random.normal(0.95, 0.05)
        elif gesture_id == 1: # Closed Fist: all fingers curled (~0.0)
            t = np.random.normal(0.1, 0.05)
            i = np.random.normal(0.05, 0.04)
            m = np.random.normal(0.05, 0.04)
            r = np.random.normal(0.05, 0.04)
            p = np.random.normal(0.05, 0.04)
        elif gesture_id == 2: # Peace Sign: Index & Middle extended (~1.0), others curled (~0.0)
            t = np.random.normal(0.15, 0.05)
            i = np.random.normal(0.95, 0.05)
            m = np.random.normal(0.95, 0.05)
            r = np.random.normal(0.1, 0.04)
            p = np.random.normal(0.1, 0.04)
        elif gesture_id == 3: # Thumbs Up: Thumb extended (~1.0), others curled (~0.0)
            t = np.random.normal(0.95, 0.05)
            i = np.random.normal(0.1, 0.04)
            m = np.random.normal(0.1, 0.04)
            r = np.random.normal(0.1, 0.04)
            p = np.random.normal(0.1, 0.04)
        else:                # OK Sign: Thumb & Index touching (~0.2), Middle/Ring/Pinky extended (~0.9)
            t = np.random.normal(0.2, 0.05)
            i = np.random.normal(0.2, 0.05)
            m = np.random.normal(0.9, 0.05)
            r = np.random.normal(0.9, 0.05)
            p = np.random.normal(0.9, 0.05)
            
        rows.append([round(np.clip(val, 0, 1), 3) for val in [t, i, m, r, p]] + [gesture_id])

with open(filepath, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"✅ Generated {len(rows)} hand gesture training samples in '{filepath}'")
