# Prodigy InfoTech Machine Learning Track - Task 04
## Hand Gesture Recognition Model for HCI Systems

### 📌 Overview
Develop a multi-class gesture classification model to accurately recognize hand gestures (Open Palm, Closed Fist, Peace Sign, Thumbs Up, OK Sign) from finger extension ratio vectors to enable touchless human-computer interaction (HCI).

### 🛠️ Architecture & Workflow
1. **Landmark Feature Vector**: `generate_gestures.py` extracts extension metrics for 5 digits (`thumb_ext`, `index_ext`, `middle_ext`, `ring_ext`, `pinky_ext`).
2. **Random Forest Classifier**: `train_gesture_model.py` fits an ensemble decision tree estimator on 1,250 gesture instances.
3. **Gesture Classes**:
   - Class 0: Open Palm 🖐️
   - Class 1: Closed Fist ✊
   - Class 2: Peace / V-Sign ✌️
   - Class 3: Thumbs Up 👍
   - Class 4: OK Sign 👌

### 🚀 How to Run

```bash
# Train Gesture Classifier Model
python train_gesture_model.py
```

### 📊 Model Metrics Sample
- **Accuracy**: 99.20%
- **Macro F1 Score**: 0.99
