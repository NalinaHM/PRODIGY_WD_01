import sys
import os
import random
import csv

sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('data', exist_ok=True)
filepath = os.path.join('data', 'titanic_dataset.csv')

headers = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

random.seed(42)
rows = []

first_names_male = ['John', 'William', 'James', 'Charles', 'George', 'Frank', 'Joseph', 'Thomas']
first_names_female = ['Mary', 'Anna', 'Emma', 'Elizabeth', 'Minnie', 'Margaret', 'Ida', 'Alice']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Wilson', 'Taylor', 'Anderson']

for i in range(1, 892):
    pclass = random.choices([1, 2, 3], weights=[0.24, 0.21, 0.55])[0]
    sex = random.choices(['male', 'female'], weights=[0.65, 0.35])[0]
    
    if sex == 'male':
        name = f"{random.choice(last_names)}, Mr. {random.choice(first_names_male)}"
        # Survival rate lower for adult males
        survived = 1 if random.random() < (0.35 if pclass == 1 else 0.15) else 0
    else:
        name = f"{random.choice(last_names)}, Miss. {random.choice(first_names_female)}"
        # Survival rate higher for females ("women & children first")
        survived = 1 if random.random() < (0.95 if pclass == 1 else 0.70) else 0

    # Introduce missing values in Age (~20%) and Cabin (~75%) to test data cleaning
    age = "" if random.random() < 0.20 else round(random.uniform(1, 70), 1)
    sibsp = random.choice([0, 0, 0, 1, 1, 2])
    parch = random.choice([0, 0, 0, 1, 2])
    ticket = f"A/{random.randint(1000, 9999)}"
    fare = round(random.uniform(70, 300) if pclass == 1 else (random.uniform(15, 60) if pclass == 2 else random.uniform(7, 25)), 2)
    cabin = f"{random.choice(['A','B','C','D','E'])}{random.randint(10, 99)}" if (pclass == 1 or random.random() < 0.15) else ""
    embarked = random.choices(['S', 'C', 'Q'], weights=[0.70, 0.20, 0.10])[0]

    rows.append([i, survived, pclass, name, sex, age, sibsp, parch, ticket, fare, cabin, embarked])

with open(filepath, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"[OK] Generated {len(rows)} Titanic dataset passenger records in '{filepath}'")
