import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import random
import csv
import numpy as np

os.makedirs('data', exist_ok=True)
filepath = os.path.join('data', 'dogs_vs_cats_features.csv')

# Simulate extracted image feature vectors for Dogs vs Cats image classification
# Features: Red_Mean, Green_Mean, Blue_Mean, Texture_Contrast, Aspect_Ratio, Ear_Pointiness, Tail_Length_Est
headers = ['feature_red', 'feature_green', 'feature_blue', 'texture_contrast', 'aspect_ratio', 'ear_shape', 'label']

random.seed(42)
np.random.seed(42)

rows = []
# 500 Cats (label = 0), 500 Dogs (label = 1)
for i in range(1000):
    label = 0 if i < 500 else 1
    
    if label == 0:  # Cat features
        red = np.random.normal(140, 20)
        green = np.random.normal(130, 20)
        blue = np.random.normal(120, 20)
        texture = np.random.normal(45, 10)
        aspect = np.random.normal(1.1, 0.15)
        ear = np.random.normal(0.85, 0.1)  # Pointy ears
    else:  # Dog features
        red = np.random.normal(110, 25)
        green = np.random.normal(105, 25)
        blue = np.random.normal(95, 25)
        texture = np.random.normal(70, 15)
        aspect = np.random.normal(1.4, 0.2)
        ear = np.random.normal(0.35, 0.15)  # Floppy ears
        
    rows.append([round(red, 2), round(green, 2), round(blue, 2), round(texture, 2), round(aspect, 2), round(ear, 2), label])

with open(filepath, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"✅ Generated {len(rows)} simulated image feature vectors in '{filepath}'")
