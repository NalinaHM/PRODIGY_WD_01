# Prodigy InfoTech Data Science Track - Task 02
## Data Cleaning & Exploratory Data Analysis (EDA) on Titanic Dataset

### 📌 Overview
Perform end-to-end data cleaning, handling missing values, feature engineering, and exploratory data analysis (EDA) on the Titanic passenger manifest dataset to uncover key survival trends and relationships.

### 🛠️ Data Cleaning & EDA Pipeline
1. **Missing Value Imputation**:
   - `Age`: Imputed missing values using median age per `Pclass` and `Sex` group.
   - `Embarked`: Imputed mode category.
   - `Cabin`: Extracted engineered feature `Has_Cabin`.
2. **Feature Engineering**:
   - Created `FamilySize` (`SibSp` + `Parch` + 1).
3. **Exploratory Data Analysis Insights**:
   - **Gender Bias**: Women had a ~75%+ survival rate compared to ~18% for men ("women & children first").
   - **Socio-Economic Class**: 1st Class passengers experienced higher survival rates (~62%) than 3rd Class (~24%).
   - **Family Size**: Small families (2–4 members) experienced higher survival rates than solo travelers.

### 🚀 How to Run

```bash
# Run Cleaning & EDA Script
python clean_and_eda.py
```
