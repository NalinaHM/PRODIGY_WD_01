import sys
import os
import random
import csv

sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('data', exist_ok=True)
filepath = os.path.join('data', 'population_data.csv')

headers = ['PersonID', 'Age', 'Gender', 'Country', 'Education_Level', 'Income_USD']

countries = ['USA', 'India', 'UK', 'Canada', 'Germany', 'Australia', 'Japan', 'Brazil']
education = ['High School', 'Bachelors', 'Masters', 'PhD']

random.seed(42)
rows = []

for i in range(1, 1501):
    pid = 10000 + i
    # Age distribution: skewed towards working age (18-65)
    age = int(random.triangular(18, 85, 32))
    gender = random.choices(['Male', 'Female', 'Non-Binary'], weights=[0.49, 0.49, 0.02])[0]
    country = random.choice(countries)
    edu = random.choices(education, weights=[0.25, 0.50, 0.20, 0.05])[0]
    income = round(random.lognormvariate(10.8, 0.5), 2)

    rows.append([pid, age, gender, country, edu, income])

with open(filepath, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"[OK] Generated {len(rows)} demographic population records in '{filepath}'")
