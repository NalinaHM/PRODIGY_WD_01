# Prodigy InfoTech Data Science Track - Task 04
## Social Media Sentiment Pattern Analysis & Visualization

### 📌 Overview
Analyze and visualize sentiment patterns across social media data (Positive, Negative, Neutral, Irrelevant) to evaluate public brand sentiment and track net brand polarity metrics.

### 🛠️ Analytics Workflow
1. **Dataset Generation**: `generate_sentiment_data.py` constructs social media tweet manifests labeled across major tech brands (Apple, Tesla, Google, Microsoft, Amazon, Meta).
2. **Sentiment Distribution Analysis**: `sentiment_analysis.py` computes total sentiment breakdown, crosstab sentiment matrix by brand, and social media engagement (likes/retweets).
3. **Net Sentiment Score (NSS)**: Calculates Net Sentiment Score ($\text{NSS} = \% \text{Positive} - \% \text{Negative}$) per brand.

### 🚀 How to Run

```bash
# Run Sentiment Analytics Script
python sentiment_analysis.py
```
