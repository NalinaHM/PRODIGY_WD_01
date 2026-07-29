# Prodigy InfoTech Machine Learning Track - Task 02
## Customer Segmentation using K-Means Clustering

### 📌 Overview
Group customers of a retail store based on purchase history (Annual Income vs. Spending Score) using the K-Means clustering algorithm to help retail managers create targeted marketing strategies.

### 🛠️ Architecture & Workflow
1. **Dataset Generation / Ingestion**: `generate_dataset.py` generates customer features (`Annual_Income_k`, `Spending_Score_1_100`, `Age`, `Gender`).
2. **K-Means Model & Elbow Method**: `cluster_model.py` evaluates $K \in [2, 10]$, computes WCSS / Inertia and Silhouette scores, fits optimal $K=5$ clusters, and labels customer profiles.
3. **Clustered Segments**:
   - **Cluster 0**: High Income, High Spending *(Target Segment)*
   - **Cluster 1**: Medium Income, Medium Spending *(Balanced Shoppers)*
   - **Cluster 2**: Low Income, Low Spending *(Budget Savers)*
   - **Cluster 3**: High Income, Low Spending *(High Earners / Low Spenders)*
   - **Cluster 4**: Low Income, High Spending *(Carefree Spenders)*

### 🚀 How to Run

```bash
# Train K-Means Clustering Model
python cluster_model.py
```
