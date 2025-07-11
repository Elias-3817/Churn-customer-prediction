# deployment_script.py

import os
import joblib
import pandas as pd
import numpy as np

# Load saved model and threshold
model_path = 'models/xgb_churn_model.pkl'
threshold_path = 'models/churn_threshold.pkl'

best_model = joblib.load(model_path)
best_threshold = joblib.load(threshold_path)

print(f"✅ Loaded model from {model_path}")
print(f"✅ Loaded threshold: {best_threshold:.3f}")


def predict_churn(input_data):
    """
    Takes a single customer input (as dict or DataFrame) and returns churn prediction.
    """
    if isinstance(input_data, dict):
        input_df = pd.DataFrame([input_data])
    elif isinstance(input_data, pd.DataFrame):
        input_df = input_data.copy()
    else:
        raise ValueError("Input must be a dict or a pandas DataFrame")

    # NOTE: Insert your preprocessing steps here (encoding, scaling, etc.)
    # For now, we assume input_df is already clean and ready

    probs = best_model.predict_proba(input_df)[:, 1]
    preds = (probs >= best_threshold).astype(int)

    return pd.DataFrame({
        'Churn_Probability': probs,
        'Churn_Prediction': preds
    })


# Example usage (replace with actual test sample)
if __name__ == "__main__":
    sample = {
        'gender': 'Male',
        'senior_citizen': 0,
        'tenure': 12,
        'monthly_charges': 70.5,
        'total_charges': 850.75,
        'internet_service': 'Fiber optic',
        'contract': 'Month-to-month',
        # ... add all required fields in your dataset here
    }

    print("\n📊 Churn Prediction on Sample Input")
    output = predict_churn(sample)
    print(output)
