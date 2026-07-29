import sys
import os
import random
import csv

sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('data', exist_ok=True)
filepath = os.path.join('data', 'social_media_sentiment.csv')

headers = ['TweetID', 'Brand_Topic', 'Sentiment_Label', 'Retweet_Count', 'Like_Count', 'User_Followers']

brands = ['Apple', 'Microsoft', 'Google', 'Tesla', 'Amazon', 'Meta']
sentiments = ['Positive', 'Negative', 'Neutral', 'Irrelevant']

random.seed(42)
rows = []

for i in range(1, 1201):
    tid = 100000 + i
    brand = random.choice(brands)
    
    # Skew sentiment distributions per brand for realistic EDA
    if brand == 'Tesla':
        sentiment = random.choices(sentiments, weights=[0.45, 0.40, 0.10, 0.05])[0]
    elif brand == 'Apple':
        sentiment = random.choices(sentiments, weights=[0.55, 0.20, 0.20, 0.05])[0]
    elif brand == 'Google':
        sentiment = random.choices(sentiments, weights=[0.50, 0.15, 0.30, 0.05])[0]
    else:
        sentiment = random.choices(sentiments, weights=[0.40, 0.25, 0.25, 0.10])[0]

    retweets = random.randint(0, 450)
    likes = random.randint(0, 1200)
    followers = random.randint(50, 50000)

    rows.append([tid, brand, sentiment, retweets, likes, followers])

with open(filepath, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"[OK] Generated {len(rows)} social media sentiment records in '{filepath}'")
