# Prodigy InfoTech Machine Learning Track - Task 03
## Dog vs. Cat Image Classifier using Support Vector Machines (SVM)

### 📌 Overview
Build a Support Vector Machine (SVM) binary classifier to accurately distinguish between images of **Cats 🐱** and **Dogs 🐶** based on extracted color histograms, aspect ratios, and edge density features.

### 🛠️ Architecture & Workflow
1. **Feature Extraction**: `synthetic_images.py` constructs structured feature matrices (`feature_red`, `feature_green`, `feature_blue`, `texture_contrast`, `aspect_ratio`, `ear_shape`).
2. **Preprocessing**: `StandardScaler` normalizes features.
3. **SVM Fitting**: `train_svm.py` trains an RBF-kernel SVM classifier, calculates confusion matrix metrics, precision, recall, and F1-score.
4. **Serialization**: Exports `models/dog_cat_svm_model.pkl` and `models/scaler.pkl`.

### 🚀 How to Run

```bash
# Train SVM Classifier
python train_svm.py
```

### 📊 Model Metrics Sample
- **Accuracy**: ~96.50%
- **Precision (Cat)**: 0.96 | **Recall (Cat)**: 0.97
- **Precision (Dog)**: 0.97 | **Recall (Dog)**: 0.96
