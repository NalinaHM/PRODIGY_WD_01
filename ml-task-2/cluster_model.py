import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import pickle
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 1. Load Customer Data
dataset_path = os.path.join('data', 'customer_data.csv')
if not os.path.exists(dataset_path):
    print("Dataset not found. Running dataset generator...")
    import generate_dataset

df = pd.read_csv(dataset_path)
print(f"📊 Dataset Shape: {df.shape}")
print(df.head())

# 2. Extract Features for Clustering: Annual Income & Spending Score
X = df[['Annual_Income_k', 'Spending_Score_1_100']]

# 3. Elbow Method to find optimal K (Number of Clusters)
wcss = []
silhouette_scores = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    score = silhouette_score(X, kmeans.labels_)
    silhouette_scores.append(score)

print("\n📉 Elbow Method & Silhouette Scores:")
for k, inertia, score in zip(K_range, wcss, silhouette_scores):
    print(f"   • K = {k}: WCSS (Inertia) = {inertia:.2f} | Silhouette Score = {score:.4f}")

# 4. Train K-Means with Optimal K = 5
optimal_k = 5
final_kmeans = KMeans(n_clusters=optimal_k, init='k-means++', random_state=42, n_init=10)
cluster_labels = final_kmeans.fit_predict(X)

df['Cluster'] = cluster_labels

# 5. Profile Customer Segments
print("\n👥 Customer Segment Profiles:")
segment_names = {
    0: "Target Spenders (High Income, High Spending)",
    1: "Balanced Shoppers (Medium Income, Medium Spending)",
    2: "Budget Savers (Low Income, Low Spending)",
    3: "High Earners / Low Spenders (High Income, Low Spending)",
    4: "Carefree Spenders (Low Income, High Spending)"
}

for cluster_id in range(optimal_k):
    cluster_df = df[df['Cluster'] == cluster_id]
    avg_income = cluster_df['Annual_Income_k'].mean()
    avg_spending = cluster_df['Spending_Score_1_100'].mean()
    count = len(cluster_df)
    print(f"   • Cluster {cluster_id} ({count} customers): Avg Income = ${avg_income:.1f}k, Avg Spending = {avg_spending:.1f}/100")

# 6. Save Model & Clustered Data
os.makedirs('models', exist_ok=True)
model_path = os.path.join('models', 'kmeans_model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(final_kmeans, f)

df.to_csv(os.path.join('data', 'clustered_customers.csv'), index=False)
print(f"\n💾 Model saved to '{model_path}' and clustered dataset exported.")
