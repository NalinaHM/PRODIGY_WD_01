import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import random
import csv

# Create synthetic dataset for House Price Prediction
os.makedirs('data', exist_ok=True)
filepath = os.path.join('data', 'house_prices.csv')

headers = ['square_feet', 'bedrooms', 'bathrooms', 'age_years', 'garage_spaces', 'price']

random.seed(42)

rows = []
for _ in range(1000):
    sqft = random.randint(600, 4500)
    beds = random.randint(1, 6)
    baths = random.randint(1, 4)
    age = random.randint(0, 50)
    garage = random.randint(0, 3)
    
    # Base price calculation with linear relationships and realistic noise
    base_price = (
        (sqft * 185) + 
        (beds * 25000) + 
        (baths * 35000) + 
        (garage * 15000) - 
        (age * 1200) + 
        50000
    )
    # Add random noise (+- 5%)
    noise = random.uniform(-0.05, 0.05) * base_price
    final_price = round(base_price + noise, 2)
    
    rows.append([sqft, beds, baths, age, garage, final_price])

with open(filepath, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"[OK] Generated {len(rows)} sample house records in '{filepath}'")
