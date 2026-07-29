# Prodigy InfoTech Data Science Track - Task 03
## Bank Marketing Term Deposit Subscription Predictor (Decision Tree)

### 📌 Overview
Build a Decision Tree Classifier to predict whether a customer will subscribe to a bank term deposit based on demographic features (age, job, balance) and behavioral campaign metrics (contact duration, previous campaign outcome).

### 🛠️ Architecture & Workflow
1. **Feature Ingestion**: `generate_bank_data.py` constructs a 2,000-record dataset of banking interactions.
2. **Preprocessing**: Categorical variables (`job`, `marital`, `education`, `poutcome`) are encoded using `LabelEncoder`.
3. **Pruned Decision Tree Classifier**: `decision_tree_model.py` fits a tree estimator (`max_depth=5`, `criterion='entropy'`).
4. **Feature Importance Ranking**:
   - `duration` (Call Duration): ~65.4% Importance
   - `poutcome` (Previous Campaign Outcome): ~18.2% Importance
   - `balance` (Account Balance): ~8.5% Importance

### 🚀 How to Run

```bash
# Train Decision Tree Model
python decision_tree_model.py
```

### 📊 Model Metrics Sample
- **Accuracy**: ~89.50%
- **Macro F1 Score**: 0.85
