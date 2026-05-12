import streamlit as st
import pandas as pd
import joblib

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="centered"
)

# ----------------------------
# Load Model
# ----------------------------
model = joblib.load("churn_pipeline.pkl")

# ----------------------------
# Header Section
# ----------------------------
st.title("📊 Customer Churn Prediction System")
st.markdown("""
Predict whether a customer is likely to churn using Machine Learning.
Fill in the details below and click **Predict**.
""")

st.divider()

# ----------------------------
# Input Section (Grouped UI)
# ----------------------------
st.subheader("👤 Customer Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 100, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    tenure = st.number_input("Tenure (Months)", 0, 100, 12)
    usage = st.number_input("Usage Frequency", 0, 100, 10)
    support = st.number_input("Support Calls", 0, 50, 2)

with col2:
    payment = st.number_input("Payment Delay (Days)", 0, 100, 5)
    subscription = st.selectbox("Subscription Type", ["Basic", "Standard", "Premium"])
    contract = st.selectbox("Contract Length", ["Monthly", "Quarterly", "Annual"])
    spend = st.number_input("Total Spend ($)", 0.0, value=500.0)
    interaction = st.number_input("Last Interaction (Days Ago)", 0, 365, 30)

st.divider()

# ----------------------------
# Prediction Button
# ----------------------------
if st.button("🚀 Predict Churn", use_container_width=True):

    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Tenure': [tenure],
        'Usage Frequency': [usage],
        'Support Calls': [support],
        'Payment Delay': [payment],
        'Subscription Type': [subscription],
        'Contract Length': [contract],
        'Total Spend': [spend],
        'Last Interaction': [interaction]
    })

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("📌 Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        if prediction[0] == 1:
            st.error("⚠️ Customer is likely to CHURN")
        else:
            st.success("✅ Customer is likely to STAY")
