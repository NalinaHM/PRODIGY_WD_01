import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import random
import csv

os.makedirs('data', exist_ok=True)
filepath = os.path.join('data', 'food_items.csv')

# Food classes & nutrition database (Calories per 100g, Protein, Carbs, Fat)
food_db = {
    'Pizza': {'id': 0, 'cal': 266, 'protein': 11, 'carbs': 33, 'fat': 10},
    'Salad': {'id': 1, 'cal': 45, 'protein': 2, 'carbs': 8, 'fat': 1},
    'Burger': {'id': 2, 'cal': 295, 'protein': 17, 'carbs': 30, 'fat': 14},
    'Sushi': {'id': 3, 'cal': 140, 'protein': 6, 'carbs': 28, 'fat': 1},
    'Pasta': {'id': 4, 'cal': 158, 'protein': 6, 'carbs': 31, 'fat': 1},
    'Apple': {'id': 5, 'cal': 52, 'protein': 0.3, 'carbs': 14, 'fat': 0.2},
    'Steak': {'id': 6, 'cal': 271, 'protein': 26, 'carbs': 0, 'fat': 19}
}

headers = ['red_ratio', 'green_ratio', 'blue_ratio', 'texture_smoothness', 'density_est', 'food_label', 'calories_100g']

random.seed(42)
rows = []

for food_name, info in food_db.items():
    for _ in range(200): # 200 samples per food type
        if food_name == 'Pizza':
            r, g, b = random.uniform(0.50, 0.70), random.uniform(0.20, 0.35), random.uniform(0.10, 0.25)
            tex = random.uniform(0.3, 0.6)
            den = random.uniform(0.7, 0.9)
        elif food_name == 'Salad':
            r, g, b = random.uniform(0.15, 0.30), random.uniform(0.55, 0.80), random.uniform(0.10, 0.25)
            tex = random.uniform(0.1, 0.4)
            den = random.uniform(0.3, 0.5)
        elif food_name == 'Burger':
            r, g, b = random.uniform(0.40, 0.60), random.uniform(0.25, 0.40), random.uniform(0.15, 0.30)
            tex = random.uniform(0.4, 0.7)
            den = random.uniform(0.8, 1.0)
        elif food_name == 'Sushi':
            r, g, b = random.uniform(0.20, 0.40), random.uniform(0.30, 0.50), random.uniform(0.30, 0.50)
            tex = random.uniform(0.6, 0.9)
            den = random.uniform(0.6, 0.8)
        elif food_name == 'Pasta':
            r, g, b = random.uniform(0.60, 0.80), random.uniform(0.50, 0.70), random.uniform(0.10, 0.30)
            tex = random.uniform(0.7, 0.95)
            den = random.uniform(0.6, 0.85)
        elif food_name == 'Apple':
            r, g, b = random.uniform(0.70, 0.95), random.uniform(0.10, 0.30), random.uniform(0.10, 0.25)
            tex = random.uniform(0.85, 0.98)
            den = random.uniform(0.4, 0.6)
        else: # Steak
            r, g, b = random.uniform(0.35, 0.55), random.uniform(0.10, 0.25), random.uniform(0.10, 0.25)
            tex = random.uniform(0.2, 0.5)
            den = random.uniform(0.85, 1.1)

        cal = info['cal'] + random.uniform(-5, 5)
        rows.append([round(r, 3), round(g, 3), round(b, 3), round(tex, 3), round(den, 3), food_name, round(cal, 1)])

with open(filepath, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"✅ Generated {len(rows)} food recognition items in '{filepath}'")
