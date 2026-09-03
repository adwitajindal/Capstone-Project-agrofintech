from pathlib import Path

import joblib
import pandas as pd

MODEL_DIR = Path(__file__).resolve().parent / "model"

risk_model = joblib.load(MODEL_DIR / "lending_risk_model.pkl")
loan_model = joblib.load(MODEL_DIR / "loan_prediction_model.pkl")
encoders = joblib.load(MODEL_DIR / "label_encoders.pkl")

def predict(data):
    df = pd.DataFrame([data])

    # Label Encoding
    for col, encoder in encoders.items():
        if col in df.columns:
            df[col] = encoder.transform(df[col].astype(str))

    # Risk Prediction
    risk_prediction = risk_model.predict(df)[0]

    # Loan Prediction
    loan_prediction = loan_model.predict(df)[0]

    return {
        "Risk_Level": risk_prediction.item()
        if hasattr(risk_prediction, "item")
        else risk_prediction,
        "Loan_Approval": loan_prediction.item()
        if hasattr(loan_prediction, "item")
        else loan_prediction
    }