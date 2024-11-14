import streamlit as st
import pickle
import pandas as pd
import os

# Load the pipeline (pipelist.pkl) directly
@st.cache_resource
def load_pipeline():
    pipeline_path = os.path.join(os.getcwd(), "models", "pipelist.pkl")  # Dynamic path for compatibility
    
    # Attempt to load the pipeline
    if os.path.exists(pipeline_path):
        try:
            with open(pipeline_path, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            st.error(f"An error occurred while loading the pipeline: {e}")
            return None
    else:
        st.error(f"pipelist.pkl not found at {pipeline_path}")
        return None

# Load individual model files directly from the Models folder
@st.cache_resource
def load_model(model_path):
    if os.path.exists(model_path):
        try:
            with open(model_path, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            st.error(f"An error occurred while loading the model: {e}")
            return None
    else:
        st.error(f"{model_path} not found.")
        return None


def predict_page():
    st.title("Customer Churn Prediction")
    st.sidebar.title("Predict View")
    st.sidebar.write("Predict whether a customer will churn")

    # Load the pipeline
    pipeline = load_pipeline()
    if pipeline is None:
        return  # Stop the function if pipeline loading fails

    # Model paths dictionary
    models_paths = {
        'Logistic Regression': os.path.join("models", "LR_model.pkl"),
        'RF': os.path.join("models", "RF_model.pkl"),
        'GB': os.path.join("models", "GB_model.pkl"),
        'KNN': os.path.join("models", "KNN_model.pkl"),
        'SVC': os.path.join("models", "SVC_model.pkl")
    }

    # Select and load the chosen model
    model_choice = st.selectbox("Select a model", list(models_paths.keys()))
    model = load_model(models_paths[model_choice])
    if model is None:
        return  # Stop the function if model loading fails

    st.write(f"Loaded model type: {type(model)}")

    # Single Prediction
    st.subheader("Single Customer Prediction")
    gender = st.selectbox("Gender", ['Male', 'Female'])
    senior_citizen = st.selectbox("Senior Citizen", ['Yes', 'No'])
    partner = st.selectbox("Partner", ['Yes', 'No'])
    dependents = st.selectbox("Dependents", ['Yes', 'No'])
    tenure = st.slider("Tenure (Months)", min_value=1, max_value=72, value=12)
    paperless_billing = st.selectbox("Paperless Billing", ['Yes', 'No'])
    payment_method = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
    total_charges = st.number_input("Total Charges", min_value=0.0, value=500.0)
    phone_service = st.selectbox("Phone Service", ['Yes', 'No'])
    multiple_lines = st.selectbox("Multiple Lines", ['Yes', 'No', 'No phone service'])
    internet_service = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
    online_security = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
    online_backup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
    device_protection = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
    tech_support = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
    streaming_tv = st.selectbox("Streaming TV", ['Yes', 'No', 'No internet service'])
    streaming_movies = st.selectbox("Streaming Movies", ['Yes', 'No', 'No internet service'])
    contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])

    # Prediction for single customer
    if st.button("Predict Single"):
        # Create DataFrame for the single customer
        data = pd.DataFrame({
            'Gender': [gender],
            'SeniorCitizen': [senior_citizen],
            'Partner': [partner],
            'Dependents': [dependents],
            'Tenure': [tenure],
            'PaperlessBilling': [paperless_billing],
            'PaymentMethod': [payment_method],
            'MonthlyCharges': [monthly_charges],
            'TotalCharges': [total_charges],
            'PhoneService': [phone_service],
            'MultipleLines': [multiple_lines],
            'InternetService': [internet_service],
            'OnlineSecurity': [online_security],
            'OnlineBackup': [online_backup],
            'DeviceProtection': [device_protection],
            'TechSupport': [tech_support],
            'StreamingTV': [streaming_tv],
            'StreamingMovies': [streaming_movies],
            'Contract': [contract]
        })

        # Use the pipeline to predict
        prediction = pipeline.predict(data)[0]
        probability = pipeline.predict_proba(data)[0][1] * 100

        # Display results
        st.write(f"Prediction: {'Churn' if prediction == 1 else 'Not Churn'}")
        st.write(f"Churn Probability: {probability:.2f}%")

# Entry point for Streamlit app
if __name__ == "__main__":
    predict_page()

