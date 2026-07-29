# 📊 Prodigy InfoTech - Data Science Internship Track

Official project repository containing 5 standalone Data Science tasks implemented for the Prodigy InfoTech Data Science Internship.

---

## 📂 Standalone Data Science Tasks

| Task ID | Task Title | Methodology / Analytics | Project Directory | Documentation |
| :--- | :--- | :--- | :--- | :--- |
| **DS Task 01** | **Demographic Distribution Analysis** | Continuous & Categorical Histograms / Bar Charts | [`/ds-task-1`](ds-task-1/) | [`/ds-task-1/README.md`](ds-task-1/README.md) |
| **DS Task 02** | **Titanic Data Cleaning & EDA** | Imputation, Feature Engineering & Survival Trends | [`/ds-task-2`](ds-task-2/) | [`/ds-task-2/README.md`](ds-task-2/README.md) |
| **DS Task 03** | **Bank Marketing Decision Tree** | Pruned Entropy Decision Tree Classifier | [`/ds-task-3`](ds-task-3/) | [`/ds-task-3/README.md`](ds-task-3/README.md) |
| **DS Task 04** | **Social Media Sentiment Analysis** | Brand Polarity Crosstab & Net Sentiment Score | [`/ds-task-4`](ds-task-4/) | [`/ds-task-4/README.md`](ds-task-4/README.md) |
| **DS Task 05** | **Traffic Accident Hotspot Analysis** | Rush Hour Temporal & Weather Hotspot Analysis | [`/ds-task-5`](ds-task-5/) | [`/ds-task-5/README.md`](ds-task-5/README.md) |

---

## 🛠️ Summary & Execution Details

### 📊 DS Task 01: Demographic Distribution Analysis
- **Goal**: Analyze age, gender, education, and income distributions across 1,500 population samples.
- **Quick Run**:
  ```bash
  cd ds-task-1
  python analyze_visualize.py
  ```

### 🚢 DS Task 02: Titanic Data Cleaning & EDA
- **Goal**: Impute missing ages per class/sex, engineer family size features, and identify survival factors ("women & children first", socio-economic class bias).
- **Quick Run**:
  ```bash
  cd ds-task-2
  python clean_and_eda.py
  ```

### 🌳 DS Task 03: Bank Marketing Decision Tree Classifier
- **Goal**: Predict term deposit subscriptions using a decision tree model (`max_depth=5`, Accuracy = 89.5%).
- **Quick Run**:
  ```bash
  cd ds-task-3
  python decision_tree_model.py
  ```

### 💬 DS Task 04: Social Media Sentiment Analysis
- **Goal**: Analyze tweet sentiment breakdown across tech brands and compute Net Sentiment Scores ($\text{NSS} = \% \text{Positive} - \% \text{Negative}$).
- **Quick Run**:
  ```bash
  cd ds-task-4
  python sentiment_analysis.py
  ```

### 🚗 DS Task 05: Traffic Accident Hotspot Analysis
- **Goal**: Identify peak commuter risk hours (7-8 AM & 4-5 PM rush hours), adverse weather severity impact, and top hotspot metro cities.
- **Quick Run**:
  ```bash
  cd ds-task-5
  python accident_analysis.py
  ```
