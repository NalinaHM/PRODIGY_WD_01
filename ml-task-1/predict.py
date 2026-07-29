import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import pickle
import pandas as pd

def predict_house_price():
    model_path = os.path.join('models', 'linear_regression_model.pkl')
    if not os.path.exists(model_path):
        print("Model file not found. Running training script...")
        import model

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    print("==================================================")
    print("🏠 House Price Predictor - Prodigy ML Task 01")
    print("==================================================")

    try:
        sqft = float(input("Enter Square Feet (e.g. 2000): "))
        beds = int(input("Enter Number of Bedrooms (e.g. 3): "))
        baths = int(input("Enter Number of Bathrooms (e.g. 2): "))
        age = int(input("Enter House Age in Years (e.g. 10): "))
        garage = int(input("Enter Garage Capacity (0-3): "))

        input_data = pd.DataFrame([[sqft, beds, baths, age, garage]], 
                                  columns=['square_feet', 'bedrooms', 'bathrooms', 'age_years', 'garage_spaces'])
        
        predicted_price = model.predict(input_data)[0]

        print("\n💰 PREDICTED HOUSE PRICE:")
        print(f"   ${predicted_price:,.2f}")
        print("==================================================")
    except Exception as e:
        print(f"❌ Invalid Input: {e}")

if __name__ == "__main__":
    predict_house_price()
