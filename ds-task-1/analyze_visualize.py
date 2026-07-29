import sys
import os
import pandas as pd
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load Population Data
dataset_path = os.path.join('data', 'population_data.csv')
if not os.path.exists(dataset_path):
    print("Dataset not found. Generating population sample...")
    import generate_data

df = pd.read_csv(dataset_path)
print("==================================================")
print("📊 Data Science Task 01: Demographic Distribution Analysis")
print("==================================================")
print(f"Total Dataset Size: {len(df)} records")
print(df.head())

# 2. Continuous Variable Analysis: Age Distribution (Histogram Binning)
print("\n📈 Continuous Variable Analysis: Age Distribution (Histogram)")
age_bins = [18, 25, 35, 45, 55, 65, 100]
age_labels = ['18-24 (Young Adult)', '25-34 (Early Career)', '35-44 (Mid Career)', '45-54 (Senior)', '55-64 (Pre-Retirement)', '65+ (Senior Citizen)']
df['Age_Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)

age_dist = df['Age_Group'].value_counts().sort_index()
print(age_dist)

# 3. Categorical Variable Analysis: Gender & Education Bar Chart Counts
print("\n📊 Categorical Variable Analysis: Gender Distribution")
gender_dist = df['Gender'].value_counts()
print(gender_dist)

print("\n🎓 Categorical Variable Analysis: Education Level Distribution")
edu_dist = df['Education_Level'].value_counts()
print(edu_dist)

print("\n🌍 Categorical Variable Analysis: Top Countries")
country_dist = df['Country'].value_counts()
print(country_dist)

# Summary Stats
print("\n💰 Continuous Variable Summary: Income ($)")
print(f"   • Mean Income:   ${df['Income_USD'].mean():,.2f}")
print(f"   • Median Income: ${df['Income_USD'].median():,.2f}")
print(f"   • Min / Max:     ${df['Income_USD'].min():,.2f} / ${df['Income_USD'].max():,.2f}")

print("\n[OK] Demographic distribution analysis completed successfully.")
