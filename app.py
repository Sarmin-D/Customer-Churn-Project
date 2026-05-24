# ============================================
# STREAMLIT CUSTOMER CHURN UI
# ============================================

# IMPORT LIBRARIES
import streamlit as st
import requests

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# ============================================
# CUSTOM CSS
# ============================================

st.markdown(
    """
    <style>

    .main {
        background-color: #0E1117;
    }

    h1 {
        color: white;
        text-align: center;
    }

    .stButton>button {
        width: 100%;
        height: 50px;
        background-color: #00ADB5;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        border: none;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================
# TITLE
# ============================================

st.title("📊 Customer Churn Prediction System")

st.write(
    "AI Powered Customer Retention Prediction Dashboard"
)

# ============================================
# SIDEBAR
# ============================================

st.sidebar.header("Customer Information")

# ============================================
# INPUT FIELDS
# ============================================

gender = st.sidebar.selectbox(
    "Gender",
     ["Male", "Female"]
)

senior = st.sidebar.selectbox(
    "Senior Citizen",
    ["No", "Yes"]
)

partner = st.sidebar.selectbox(
    "Partner",
    ["Yes", "No"]
)

dependents = st.sidebar.selectbox(
    "Dependents",
    ["Yes", "No"]
)

tenure = st.sidebar.number_input(
    "Customer Tenure (Months)",
    min_value=0,
    max_value=72,
    value=12,
    help="Enter customer tenure in months"
)

phone_service = st.sidebar.selectbox(
    "Phone Service",
    ["No", "Yes"]
)

multiple_lines = st.sidebar.selectbox(
    "Multiple Lines",
    ["No", "Yes"]
)

internet_service = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber Optic", "No"]
)

online_security = st.sidebar.selectbox(
    "Online Security",
    ["No", "Yes"]
)

online_backup = st.sidebar.selectbox(
    "Online Backup",
    ["No", "Yes"]
)

device_protection = st.sidebar.selectbox(
    "Device Protection",
    ["No", "Yes"]
)

tech_support = st.sidebar.selectbox(
    "Tech Support",
    ["No", "Yes"]
)

streaming_tv = st.sidebar.selectbox(
    "Streaming TV",
    ["No", "Yes"]
)

streaming_movies = st.sidebar.selectbox(
    "Streaming Movies",
    ["No", "Yes"]
)

contract = st.sidebar.selectbox(
    "Contract Type",
    [
        "Month-to-Month",
        "One Year",
        "Two Year"
    ]
)

paperless_billing = st.sidebar.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)

payment_method = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic Check",
        "Mailed Check",
        "Bank Transfer",
        "Credit Card"
    ]
)

monthly_charges = st.sidebar.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

total_charges = st.sidebar.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)

# ============================================
# CONVERT TEXT VALUES INTO NUMBERS
# ============================================

senior = 1 if senior == "Yes" else 0

partner = 1 if partner == "Yes" else 0

dependents = 1 if dependents == "Yes" else 0

phone_service = 1 if phone_service == "Yes" else 0

multiple_lines = 1 if multiple_lines == "Yes" else 0

online_security = 1 if online_security == "Yes" else 0

online_backup = 1 if online_backup == "Yes" else 0

device_protection = 1 if device_protection == "Yes" else 0

tech_support = 1 if tech_support == "Yes" else 0

streaming_tv = 1 if streaming_tv == "Yes" else 0

streaming_movies = 1 if streaming_movies == "Yes" else 0

paperless_billing = 1 if paperless_billing == "Yes" else 0

#Gender
gender_map = {
    "Male" : 0,
    "Female" : 1
}

gender = gender_map[gender]

# INTERNET SERVICE

internet_map = {
    "DSL": 0,
    "Fiber Optic": 1,
    "No": 2
}

internet_service = internet_map[internet_service]

# CONTRACT TYPE

contract_map = {
    "Month-to-Month": 0,
    "One Year": 1,
    "Two Year": 2
}

contract = contract_map[contract]

# PAYMENT METHOD

payment_map = {
    "Electronic Check": 0,
    "Mailed Check": 1,
    "Bank Transfer": 2,
    "Credit Card": 3
}

payment_method = payment_map[payment_method]

# ============================================
# PREDICT BUTTON
# ============================================

if st.button("Predict Churn"):

    # API URL
    url = "http://127.0.0.1:8000/predict"

    # INPUT DATA
    data = {
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }





#  # ============================================
#     # API REQUEST
#     # ============================================

#     try:

#         response = requests.post(
#             url,
#             json=data
#         )

#         result = response.json()

#         prediction = result["prediction"]

#         # ============================================
#         # RESULT SHOW 
#         # ============================================

#         if prediction == "Customer May Churn":

#             st.error(
#                 "⚠ Customer May Churn"
#             )

#         else:

#             st.success(
#                 "✅ Customer Will Stay"
#             )

#     except:

#         st.error(
#             "❌ FastAPI Backend Running Nahi Hai"
#         )







    # SEND REQUEST
    response = requests.post(
        url,
        json=data
    )

    # GET RESULT
    result = response.json()

    prediction = result["prediction"]

    # SHOW RESULT
    if prediction == "Customer May Churn":

        st.error(
            "⚠ Customer May Churn"
        )

    else:

        st.success(
            "✅ Customer Will Stay"
        )