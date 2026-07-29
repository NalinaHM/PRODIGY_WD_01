import sys
import os
import random
import csv

sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('data', exist_ok=True)
filepath = os.path.join('data', 'traffic_accidents.csv')

headers = ['Accident_ID', 'Severity', 'State', 'City', 'Weather_Condition', 'Road_Condition', 'Light_Condition', 'Hour_Of_Day', 'Is_Weekend']

states_cities = [
  ('CA', 'Los Angeles'), ('CA', 'San Diego'), ('TX', 'Houston'), ('FL', 'Miami'),
  ('NY', 'New York'), ('IL', 'Chicago'), ('AZ', 'Phoenix'), ('NC', 'Charlotte')
]
weather_types = ['Clear', 'Rain', 'Heavy Rain', 'Snow', 'Fog', 'Overcast']
road_types = ['Dry', 'Wet', 'Icy', 'Snow Cover', 'Construction Zone', 'Loose Gravel']
light_types = ['Daylight', 'Dark - Street Lights', 'Dark - No Lights', 'Dusk', 'Dawn']

random.seed(42)
rows = []

for i in range(1, 2501):
    aid = f"A-{100000 + i}"
    state, city = random.choice(states_cities)

    # Hour distribution: peaks during morning (7-9 AM) and evening rush hours (4-7 PM)
    hour = random.choices(
        range(24),
        weights=[2, 1, 1, 1, 2, 4, 7, 10, 9, 6, 5, 5, 6, 6, 7, 9, 10, 8, 6, 4, 3, 3, 2, 2]
    )[0]

    weekend = 1 if random.random() < 0.28 else 0
    weather = random.choices(weather_types, weights=[0.50, 0.20, 0.08, 0.10, 0.07, 0.05])[0]

    if weather in ['Rain', 'Heavy Rain']:
        road = random.choices(['Wet', 'Construction Zone'], weights=[0.85, 0.15])[0]
    elif weather == 'Snow':
        road = random.choices(['Icy', 'Snow Cover'], weights=[0.60, 0.40])[0]
    else:
        road = random.choices(['Dry', 'Wet', 'Construction Zone'], weights=[0.80, 0.10, 0.10])[0]

    if 6 <= hour <= 18:
        light = 'Daylight'
    elif hour in [5, 19]:
        light = random.choice(['Dusk', 'Dawn'])
    else:
        light = random.choices(['Dark - Street Lights', 'Dark - No Lights'], weights=[0.80, 0.20])[0]

    # Severity scale (1: Minor, 2: Moderate, 3: Serious, 4: Severe)
    prob_sev = [0.40, 0.40, 0.15, 0.05]
    if weather in ['Heavy Rain', 'Snow', 'Fog']: prob_sev = [0.15, 0.35, 0.35, 0.15]
    if road in ['Icy', 'Construction Zone']: prob_sev = [0.10, 0.30, 0.40, 0.20]

    severity = random.choices([1, 2, 3, 4], weights=prob_sev)[0]

    rows.append([aid, severity, state, city, weather, road, light, hour, weekend])

with open(filepath, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"[OK] Generated {len(rows)} traffic accident incident records in '{filepath}'")
