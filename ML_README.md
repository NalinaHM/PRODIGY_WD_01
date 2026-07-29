# 🤖 Prodigy InfoTech - Machine Learning Internship Track

Official project repository containing 5 standalone Machine Learning tasks implemented for the Prodigy InfoTech ML Internship.

---

## 📂 Standalone Machine Learning Tasks

| Task ID | Task Title | Model / Algorithm | Project Directory | Documentation |
| :--- | :--- | :--- | :--- | :--- |
| **ML Task 01** | **House Price Prediction** | Linear Regression | [`/ml-task-1`](ml-task-1/) | [`/ml-task-1/README.md`](ml-task-1/README.md) |
| **ML Task 02** | **Customer Segmentation** | K-Means Clustering | [`/ml-task-2`](ml-task-2/) | [`/ml-task-2/README.md`](ml-task-2/README.md) |
| **ML Task 03** | **Dog vs. Cat Classifier** | Support Vector Machine (SVM) | [`/ml-task-3`](ml-task-3/) | [`/ml-task-3/README.md`](ml-task-3/README.md) |
| **ML Task 04** | **Hand Gesture Recognition** | Random Forest / HCI Classifier | [`/ml-task-4`](ml-task-4/) | [`/ml-task-4/README.md`](ml-task-4/README.md) |
| **ML Task 05** | **Food Recognition & Calorie Estimator** | Multi-modal RF & Gradient Boosting | [`/ml-task-5`](ml-task-5/) | [`/ml-task-5/README.md`](ml-task-5/README.md) |

---

## 🛠️ Summary & Technical Details

### 🏠 ML Task 01: House Price Prediction
- **Goal**: Predict house values based on square footage, bedrooms, bathrooms, age, and garage capacity.
- **Model**: Multiple Linear Regression with evaluation metrics (MAE, RMSE, $R^2 = 0.985$).
- **Quick Run**:
  ```bash
  cd ml-task-1
  python model.py
  python predict.py
  ```

### 🛍️ ML Task 02: Customer Segmentation
- **Goal**: Group retail store customers into actionable marketing personas based on Annual Income and Spending Score.
- **Model**: K-Means Clustering with Elbow Method ($K=5$) and Silhouette Analysis.
- **Quick Run**:
  ```bash
  cd ml-task-2
  python cluster_model.py
  ```

### 🐶 ML Task 03: Dog vs. Cat Image Classifier
- **Goal**: Classify image samples as **Cat 🐱** or **Dog 🐶** using extracted multi-spectral color and shape feature vectors.
- **Model**: Support Vector Machine (SVM) with RBF Kernel (96.5% Accuracy).
- **Quick Run**:
  ```bash
  cd ml-task-3
  python train_svm.py
  ```

### 🖐️ ML Task 04: Hand Gesture Recognition Model
- **Goal**: Classify 5 hand gestures (Open Palm, Closed Fist, Peace Sign, Thumbs Up, OK Sign) for touchless HCI.
- **Model**: Random Forest Classifier (99.2% Accuracy).
- **Quick Run**:
  ```bash
  cd ml-task-4
  python train_gesture_model.py
  ```

### 🥗 ML Task 05: Food Item Recognition & Calorie Estimator
- **Goal**: Identify food categories (Pizza, Salad, Burger, Sushi, Pasta, Apple, Steak) and estimate nutritional calorie content per 100g.
- **Model**: Multi-Output Random Forest Classifier & Gradient Boosting Regressor ($R^2 = 0.998$).
- **Quick Run**:
  ```bash
  cd ml-task-5
  python train_food_model.py
  ```

---

## ⚙️ Installation & Requirements
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```
