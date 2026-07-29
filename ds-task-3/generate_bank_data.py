import sys
import os
import random
import csv

sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('data', exist_ok=True)
filepath = os.path.join('data', 'bank_marketing.csv')

headers = ['age', 'job', 'marital', 'education', 'default', 'balance', 'housing', 'loan', 'contact', 'duration', 'campaign', 'poutcome', 'deposit_subscribed']

jobs = ['admin.', 'blue-collar', 'technician', 'services', 'management', 'retired', 'entrepreneur', 'self-employed']
maritals = ['single', 'married', 'divorced']
educations = ['primary', 'secondary', 'tertiary']
contacts = ['cellular', 'telephone']
poutcomes = ['unknown', 'failure', 'other', 'success']

random.seed(42)
rows = []

for _ in range(2000):
    age = random.randint(18, 70)
    job = random.choice(jobs)
    marital = random.choice(maritals)
    edu = random.choice(educations)
    default = 'yes' if random.random() < 0.02 else 'no'
    balance = random.randint(-500, 15000)
    housing = 'yes' if random.random() < 0.55 else 'no'
    loan = 'yes' if random.random() < 0.15 else 'no'
    contact = random.choice(contacts)
    duration = random.randint(30, 1200) # Call duration in seconds
    campaign = random.randint(1, 6)
    poutcome = random.choices(poutcomes, weights=[0.70, 0.15, 0.08, 0.07])[0]

    # Target logic: longer duration, higher balance, and success in previous campaign lead to subscription
    prob = 0.05
    if duration > 300: prob += 0.25
    if duration > 600: prob += 0.30
    if poutcome == 'success': prob += 0.35
    if balance > 3000: prob += 0.10
    if housing == 'no': prob += 0.05

    subscribed = 'yes' if random.random() < prob else 'no'
    rows.append([age, job, marital, edu, default, balance, housing, loan, contact, duration, campaign, poutcome, subscribed])

with open(filepath, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"[OK] Generated {len(rows)} Bank Marketing campaign records in '{filepath}'")
