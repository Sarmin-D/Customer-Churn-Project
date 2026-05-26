# ============================================
# FASTAPI CUSTOMER CHURN BACKEND
# ============================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib

# ============================================
# APP INIT
# ============================================

app = FastAPI(
    title="Customer Churn Prediction API"
)

# ============================================
# LOAD MODEL + SCALER
# ============================================

try:
    model = joblib.load("Churn_model.pkl")
    scaler = joblib.load("scaler.pkl")

except Exception as e:
    print("Model loading error:", e)
    model = None
    scaler = None

# ============================================
# INPUT SCHEMA
# ============================================

class CustomerData(BaseModel):

    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: float
    PhoneService: int
    MultipleLines: int
    InternetService: int
    OnlineSecurity: int
    OnlineBackup: int
    DeviceProtection: int
    TechSupport: int
    StreamingTV: int
    StreamingMovies: int
    Contract: int
    PaperlessBilling: int
    PaymentMethod: int
    MonthlyCharges: float
    TotalCharges: float

# ============================================
# HOME ROUTE
# ============================================

@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API Running"}

# ============================================
# PREDICTION ROUTE (WITH EXCEPTION HANDLING)
# ============================================

@app.post("/predict")
def predict(data: CustomerData):

    try:

        if model is None or scaler is None:
            raise HTTPException(
                status_code=500,
                detail="Model or scaler not loaded properly"
            )

        # INPUT ARRAY
        input_data = np.array([[

            data.gender,
            data.SeniorCitizen,
            data.Partner,
            data.Dependents,
            data.tenure,
            data.PhoneService,
            data.MultipleLines,
            data.InternetService,
            data.OnlineSecurity,
            data.OnlineBackup,
            data.DeviceProtection,
            data.TechSupport,
            data.StreamingTV,
            data.StreamingMovies,
            data.Contract,
            data.PaperlessBilling,
            data.PaymentMethod,
            data.MonthlyCharges,
            data.TotalCharges

        ]])

        # SCALE
        scaled_data = scaler.transform(input_data)

        # PREDICTION
        prediction = model.predict(scaled_data)[0]

        # PROBABILITY
        probability = model.predict_proba(scaled_data)[0][1]

        # RESULT
        result = "Customer May Churn" if prediction == 1 else "Customer Will Stay"

        return {
            "prediction": result,
            "probability": float(probability)
        }

    except HTTPException as he:
        raise he

    except Exception as e:
        print("Prediction error:", e)
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )