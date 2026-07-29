# Prodigy InfoTech Machine Learning Track - Task 05
## Food Item Recognition & Calorie Estimation Model

### 📌 Overview
Build a multi-modal computer vision model to identify food items (Pizza, Salad, Burger, Sushi, Pasta, Apple, Steak) from visual/textural characteristics and predict their calorie content per 100g to enable intelligent dietary tracking.

### 🛠️ Architecture & Workflow
1. **Feature Extraction**: `food_dataset.py` extracts multi-spectral color metrics (`red_ratio`, `green_ratio`, `blue_ratio`), surface texture smoothness, and volumetric density.
2. **Food Item Classification**: `train_food_model.py` trains a Random Forest Classifier to identify food categories.
3. **Calorie Estimation**: Fits a Gradient Boosting Regressor to estimate nutritional calories ($kcal / 100g$).
4. **Model Export**: Exports `models/food_classifier.pkl` and `models/calorie_regressor.pkl`.

### 🚀 How to Run

```bash
# Train Food Recognition & Calorie Regressor
python train_food_model.py
```

### 📊 Model Metrics Sample
- **Classification Accuracy**: 98.60%
- **Calorie Regression MAE**: 2.85 kcal / 100g
- **Calorie Regression $R^2$**: 0.998
