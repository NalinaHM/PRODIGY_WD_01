import sys
import os
import pandas as pd
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load Social Media Data
dataset_path = os.path.join('data', 'social_media_sentiment.csv')
if not os.path.exists(dataset_path):
    print("Dataset not found. Generating sentiment dataset...")
    import generate_sentiment_data

df = pd.read_csv(dataset_path)
print("==================================================")
print("💬 Data Science Task 04: Social Media Sentiment Analysis")
print("==================================================")
print(f"Total Tweets Analyzed: {len(df)}")
print(df.head())

# 2. Overall Sentiment Distribution
print("\n📊 Overall Sentiment Breakdown:")
sentiment_counts = df['Sentiment_Label'].value_counts()
sentiment_percentages = (df['Sentiment_Label'].value_counts(normalize=True) * 100).round(2)

for sentiment, pct in sentiment_percentages.items():
    count = sentiment_counts[sentiment]
    print(f"   • {sentiment:12s}: {pct:5.2f}% ({count} tweets)")

# 3. Sentiment Analysis Per Brand Topic
print("\n🏷️ Sentiment Matrix By Brand / Topic:")
brand_sentiment = pd.crosstab(df['Brand_Topic'], df['Sentiment_Label'], normalize='index') * 100
print(brand_sentiment.round(2).astype(str) + '%')

# 4. Engagement Analysis (Likes & Retweets by Sentiment)
print("\n🔥 Average User Engagement (Likes & Retweets) by Sentiment:")
engagement = df.groupby('Sentiment_Label')[['Like_Count', 'Retweet_Count']].mean().round(1)
print(engagement)

# 5. Net Sentiment Score (NSS = % Positive - % Negative)
print("\n📈 Net Sentiment Score (NSS = % Positive - % Negative) by Brand:")
for brand in df['Brand_Topic'].unique():
    brand_df = df[df['Brand_Topic'] == brand]
    pos_pct = (brand_df['Sentiment_Label'] == 'Positive').mean() * 100
    neg_pct = (brand_df['Sentiment_Label'] == 'Negative').mean() * 100
    nss = pos_pct - neg_pct
    print(f"   • {brand:12s}: NSS = {nss:+6.2f}% (Pos: {pos_pct:.1f}%, Neg: {neg_pct:.1f}%)")

print("\n[OK] Social Media Sentiment Analysis completed successfully.")
