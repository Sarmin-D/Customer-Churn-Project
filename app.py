# ============================================
# STREAMLIT CUSTOMER CHURN UI
# ============================================

# ============================================
# IMPORT LIBRARIES
# ============================================

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
    ["No", "Yes"]
)

dependents = st.sidebar.selectbox(
    "Dependents",
    ["No", "Yes"]
)

tenure = st.sidebar.number_input(
    "Customer Tenure (Months)",
    min_value=0,
    max_value=120,
    value=12,
    help="Customer kitne months se service use kar raha hai"
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
# TEXT VALUES KO NUMBERS ME CONVERT KARNA
# ============================================

# GENDER MAPPING

gender_map = {
    "Male": 0,
    "Female": 1
}

gender = gender_map[gender]

# YES / NO VALUES

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

# INTERNET SERVICE MAPPING

internet_map = {
    "DSL": 0,
    "Fiber Optic": 1,
    "No": 2
}

internet_service = internet_map[internet_service]

# CONTRACT TYPE MAPPING

contract_map = {
    "Month-to-Month": 0,
    "One Year": 1,
    "Two Year": 2
}

contract = contract_map[contract]

# PAYMENT METHOD MAPPING

payment_map = {
    "Electronic Check": 0,
    "Mailed Check": 1,
    "Bank Transfer": 2,
    "Credit Card": 3
}

payment_method = payment_map[payment_method]

# ============================================
# PREDICT BUTTON (FINAL CLEAN VERSION)
# ============================================

if "total" not in st.session_state:
    st.session_state.total = 0

if "churn" not in st.session_state:
    st.session_state.churn = 0

if "stay" not in st.session_state:
    st.session_state.stay = 0



if st.button("Predict Churn"):

    url = "http://127.0.0.1:8000/predict"

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

    try:
        response = requests.post(url, json=data, timeout=60)
        response.raise_for_status()

        result = response.json()

        prediction = result["prediction"]

        # ✅ REAL probability from backend (no random)
        probability = result.get("probability", 0)

        # ============================================
        # UPDATE STATS
        # ============================================

        st.session_state.total += 1

        if prediction == "Customer May Churn":
            st.session_state.churn += 1
        else:
            st.session_state.stay += 1

        # ============================================
        # DASHBOARD
        # ============================================

        st.markdown("## 📊 Dashboard Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Predictions", st.session_state.total)
        col2.metric("Will Stay", st.session_state.stay)
        col3.metric("Will Churn", st.session_state.churn)

        # ============================================
        # PROBABILITY
        # ============================================

        st.markdown("## 🎯 Churn Probability")

        st.progress(probability)

        st.write(f"Risk Score: {round(probability * 100, 2)}%")

        if probability < 0.4:
            risk = "🟢 Low Risk"
        elif probability < 0.7:
            risk = "🟡 Medium Risk"
        else:
            risk = "🔴 High Risk"

        st.write("Risk Level:", risk)

        # ============================================
        # RESULT
        # ============================================

        if prediction == "Customer May Churn":
            st.error("⚠ Customer May Churn")
        else:
            st.success("✅ Customer Will Stay")

    except requests.exceptions.ConnectionError:
        st.error("❌ Backend server not responding (FastAPI is down)")

    except requests.exceptions.Timeout:
        st.error("⏰ Request timeout over")

    except Exception as e:
        st.error(f"❌ Unexpected error: {str(e)}")