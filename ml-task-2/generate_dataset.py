import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import random
import csv

os.makedirs('data', exist_ok=True)
filepath = os.path.join('data', 'customer_data.csv')

headers = ['CustomerID', 'Gender', 'Age', 'Annual_Income_k', 'Spending_Score_1_100']

random.seed(42)
rows = []

# Generate 5 realistic customer persona clusters for Mall/Retail dataset
# Cluster 1: Low Income, Low Spending
# Cluster 2: Low Income, High Spending
# Cluster 3: Medium Income, Medium Spending
# Cluster 4: High Income, Low Spending
# Cluster 5: High Income, High Spending

for i in range(1, 301):
    gender = random.choice(['Male', 'Female'])
    age = random.randint(18, 70)
    
    # Pick a random persona profile
    persona = random.choice([1, 2, 3, 4, 5])
    if persona == 1:
        income = random.randint(15, 40)
        spending = random.randint(5, 39)
    elif persona == 2:
        income = random.randint(15, 40)
        spending = random.randint(60, 98)
    elif persona == 3:
        income = random.randint(45, 75)
        spending = random.randint(40, 60)
    elif persona == 4:
        income = random.randint(80, 137)
        spending = random.randint(5, 39)
    else: # persona == 5
        income = random.randint(80, 137)
        spending = random.randint(60, 98)
        
    rows.append([1000 + i, gender, age, income, spending])

with open(filepath, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"✅ Generated {len(rows)} retail customer records in '{filepath}'")
