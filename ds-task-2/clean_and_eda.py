import sys
import os
import pandas as pd
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load Raw Titanic Dataset
dataset_path = os.path.join('data', 'titanic_dataset.csv')
if not os.path.exists(dataset_path):
    print("Dataset not found. Generating Titanic dataset sample...")
    import generate_titanic

df = pd.read_csv(dataset_path)
print("==================================================")
print("🚢 Data Science Task 02: Titanic Data Cleaning & EDA")
print("==================================================")
print(f"Raw Dataset Shape: {df.shape}")
print(df.info())

# 2. DATA CLEANING PHASE
print("\n🧹 PHASE 1: Data Cleaning & Missing Value Imputation")

# Check missing values
missing_before = df.isnull().sum()
print("Missing values before cleaning:")
print(missing_before[missing_before > 0])

# Impute missing Age with median Age per Pclass and Sex
median_ages = df.groupby(['Pclass', 'Sex'])['Age'].transform('median')
df['Age'] = df['Age'].fillna(median_ages)

# Handle Cabin column (High null count -> create Has_Cabin feature flag)
df['Has_Cabin'] = df['Cabin'].notnull().astype(int)

# Impute missing Embarked with mode
mode_embarked = df['Embarked'].mode()[0]
df['Embarked'] = df['Embarked'].fillna(mode_embarked)

# Create Family Size feature
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# Check missing values after cleaning
missing_after = df.isnull().sum()
print("\nMissing values after cleaning:")
print(missing_after[missing_after > 0])

# Export Clean Dataset
clean_path = os.path.join('data', 'titanic_cleaned.csv')
df.to_csv(clean_path, index=False)
print(f"\n[OK] Cleaned dataset saved to '{clean_path}'")

# 3. EXPLORATORY DATA ANALYSIS (EDA) PHASE
print("\n📊 PHASE 2: Exploratory Data Analysis & Pattern Identification")

overall_survival = df['Survived'].mean() * 100
print(f"   • Overall Survival Rate: {overall_survival:.2f}%")

print("\n1. Survival Rate by Gender:")
sex_survival = df.groupby('Sex')['Survived'].agg(['count', 'mean']).rename(columns={'mean': 'Survival_Rate'})
sex_survival['Survival_Rate'] = (sex_survival['Survival_Rate'] * 100).round(2).astype(str) + '%'
print(sex_survival)

print("\n2. Survival Rate by Passenger Class (Pclass):")
pclass_survival = df.groupby('Pclass')['Survived'].agg(['count', 'mean']).rename(columns={'mean': 'Survival_Rate'})
pclass_survival['Survival_Rate'] = (pclass_survival['Survival_Rate'] * 100).round(2).astype(str) + '%'
print(pclass_survival)

print("\n3. Survival Rate by Gender and Class Combination:")
pivot_survival = df.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='mean')
print((pivot_survival * 100).round(2).astype(str) + '%')

print("\n4. Survival Rate by Family Size:")
fam_survival = df.groupby('FamilySize')['Survived'].agg(['count', 'mean']).rename(columns={'mean': 'Survival_Rate'})
fam_survival['Survival_Rate'] = (fam_survival['Survival_Rate'] * 100).round(2).astype(str) + '%'
print(fam_survival)

print("\n💡 Key Insights Discovered:")
print("   • Female passengers had a significantly higher survival rate than male passengers.")
print("   • 1st Class passengers prioritized higher survival rates compared to 3rd Class.")
print("   • Passengers traveling in small families (2-4 members) had better survival odds than solo travelers or large families.")
