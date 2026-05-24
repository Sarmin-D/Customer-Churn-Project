# ============================================
# FASTAPI CUSTOMER CHURN BACKEND
# ============================================

# IMPORT LIBRARIES
from fastapi import FastAPI
from pydantic import BaseModel

import numpy as np
import joblib

# ============================================
# CREATE FASTAPI APP
# ============================================

app = FastAPI(
    title="Customer Churn Prediction API"
)

# ============================================
# LOAD TRAINED MODEL
# ============================================

model = joblib.load(
    "model.pkl"
)

scaler = joblib.load(
    "scaler.pkl"
)

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

    return {
        "message":
        "Customer Churn Prediction API Running"
    }

# ============================================
# PREDICTION ROUTE
# ============================================

@app.post("/predict")
def predict(data: CustomerData):

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

    # SCALE DATA
    scaled_data = scaler.transform(
        input_data
    )

    # PREDICTION
    prediction = model.predict(
        scaled_data
    )[0]

    # RESULT
    if prediction == 1:

        result = "Customer May Churn"

    else:

        result = "Customer Will Stay"

    return {
        "prediction": result
    }