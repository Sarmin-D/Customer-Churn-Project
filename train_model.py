# ============================================
# CUSTOMER CHURN MODEL TRAINING
# ============================================

# IMPORT LIBRARIES
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ============================================
# LOAD DATASET FROM GITHUB RAW URL
# ============================================

url = "https://raw.githubusercontent.com/Sarmin-D/Customer-Churn-Project/refs/heads/main/WA_Fn-UseC_-Telco-Customer-Churn%5B1%5D.csv"

df = pd.read_csv(url, on_bad_lines="skip")
print(df.head())

# ============================================
# REMOVE UNNECESSARY COLUMN
# ============================================

if "customerID" in df.columns:
    df.drop("customerID", axis=1, inplace=True)

# ============================================
# HANDLE MISSING VALUES
# ============================================

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df.dropna(inplace=True)

# ============================================
# ENCODE CATEGORICAL COLUMNS
# ============================================

encoder = LabelEncoder()

for column in df.columns:

    if df[column].dtype == "object":

        df[column] = encoder.fit_transform(
            df[column]
        )

# ============================================
# FEATURES AND TARGET
# ============================================

X = df.drop("Churn", axis=1)

y = df["Churn"]

# ============================================
# TRAIN TEST SPLIT
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ============================================
# FEATURE SCALING
# ============================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# ============================================
# TRAIN MODEL
# ============================================

model = RandomForestClassifier()

model.fit(X_train, y_train)

# ============================================
# PREDICTION
# ============================================

y_pred = model.predict(X_test)

# ============================================
# ACCURACY
# ============================================

accuracy = accuracy_score(y_test, y_pred)

print()

print("Model Accuracy:", accuracy)

# ============================================
# SAVE MODEL
# ============================================
joblib.dump(model, "Churn_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print()

print("Model Saved Successfully")