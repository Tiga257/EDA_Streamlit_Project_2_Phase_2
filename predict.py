import streamlit as st
import pickle
import pandas as pd
from imblearn import pipeline

               
# Function to load the pipeline using Streamlit's caching for better performance
@st.cache_resource
def load_pipeline():
    with open('models/pipelist copy.pkl', 'rb') as file:
        return pickle.load(file)

# Function to load a model from a given path
def load_model(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
    

# Main function to handle predictions
def predict_page():
    st.title("PREDICTION EXECUTION")
    st.sidebar.title("Customer Churn Prediction")
    st.sidebar.write("Use this app to predict whether a customer will churn or not based on their details.")

    # Load the pipeline
    pipeline = load_pipeline()

    # Available models for selection
    models_paths = {
        'Logistic Regression': 'models/LR_model.pkl',
        'Random Forest': 'models/RF_model.pkl',
        'Gradient Boosting': 'models/GB_model.pkl',
        'K-Nearest Neighbors': 'models/KNN_model.pkl',
        'Support Vector Classifier': 'models/SVC_model.pkl'
    }
                
    # Model selection via a dropdown
    model_choice = st.selectbox("Select a model", list(models_paths.keys()))
    model = load_model(models_paths[model_choice])

    if model is None:
        st.error("Failed to load the selected model")
        return

    st.write(f"**Model Loaded**: {model_choice} ({type(model)})")

    # Single Customer Prediction Section
    st.subheader("Single Customer Prediction")
    st.write("Fill in the customer details to predict whether they will churn.")

    # Collect user input for the single prediction
    customer_data = get_customer_data()

    if st.button("Predict Single"):
        if not validate_input_data(customer_data):
            st.error("Please fill in all the required fields correctly.")
            return

        # Convert input data into a DataFrame
        data = pd.DataFrame([customer_data])

        # Get the prediction and probability
        prediction = pipeline.predict(data)[0]
        probability = pipeline.predict_proba(data)[0][1] * 100

        # Display results
        st.write(f"**Prediction**: {'Churn' if prediction == 1 else 'Not Churn'}")
        st.write(f"**Churn Probability**: {probability:.2f}%")

    # Bulk Prediction Section
    st.header("Bulk Prediction")
    st.write("Upload a CSV file with customer data to predict churn for multiple customers.")

    upload_file = st.file_uploader("Upload CSV", type='csv')
    if upload_file:
        try:
            # Read the CSV file
            bulk_data = pd.read_csv(upload_file)
            st.write("**Data Preview**:", bulk_data.head())

            if validate_bulk_data(bulk_data):
                # Get predictions and probabilities for the bulk data
                bulk_predictions, bulk_probability = predict_bulk_data(pipeline, bulk_data)

                # Prepare the results
                bulk_results = bulk_data.copy()
                bulk_results["Predictions"] = ['Churn' if pred == 1 else 'Not Churn' for pred in bulk_predictions]
                bulk_results['Churned Probability'] = bulk_probability

                # Display results
                st.write("**Bulk Prediction Results**:")
                st.dataframe(bulk_results)

                # Save the results to a CSV file
                result_file = "data/bulk_predictions.csv"
                bulk_results.to_csv(result_file, index=False)
                st.success(f"Results successfully saved to `{result_file}`")
            else:
                st.error("The uploaded CSV is missing some required columns.")
        except Exception as e:
            st.error(f"Error during bulk prediction: {str(e)}")

# Helper function to get customer data from user inputs
def get_customer_data():
    customer_data = {
        'Gender': st.selectbox("Gender", ['Male', 'Female']),
        'SeniorCitizen': st.selectbox("Senior Citizen", ['Yes', 'No']),
        'Partner': st.selectbox("Partner", ['Yes', 'No']),
        'Dependents': st.selectbox("Dependents", ['Yes', 'No']),
        'Tenure': st.slider("Tenure (Months)", 1, 72, 12),
        'PaperlessBilling': st.selectbox("Paperless Billing", ['Yes', 'No']),
        'PaymentMethod': st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']),
        'MonthlyCharges': st.number_input("Monthly Charges", min_value=0.0, value=50.0),
        'TotalCharges': st.number_input("Total Charges", min_value=0.0, value=500.0),
        'PhoneService': st.selectbox("Phone Service", ['Yes', 'No']),
        'MultipleLines': st.selectbox("Multiple Lines", ['Yes', 'No', 'No phone service']),
        'InternetService': st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No']),
        'OnlineSecurity': st.selectbox("Online Security", ['Yes', 'No', 'No internet service']),
        'OnlineBackup': st.selectbox("Online Backup", ['Yes', 'No', 'No internet service']),
        'DeviceProtection': st.selectbox("Device Protection", ['Yes', 'No', 'No internet service']),
        'TechSupport': st.selectbox("Tech Support", ['Yes', 'No', 'No internet service']),
        'StreamingTV': st.selectbox("Streaming TV", ['Yes', 'No', 'No internet service']),
        'StreamingMovies': st.selectbox("Streaming Movies", ['Yes', 'No', 'No internet service']),
        'Contract': st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
    }
    return customer_data

# Function to validate input data for a single prediction
def validate_input_data(data):
    return all(data.values())

# Function to validate the bulk data
def validate_bulk_data(data):
    required_columns = [
        'Gender', 'SeniorCitizen', 'Partner', 'Dependents', 'Tenure', 'PhoneService', 'MultipleLines', 'InternetService',
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 
        'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges'
    ]
    return all(col in data.columns for col in required_columns)

# Function to predict churn for bulk data
def predict_bulk_data(pipeline, bulk_data):
    bulk_predictions = pipeline.predict(bulk_data)
    bulk_probability = pipeline.predict_proba(bulk_data)[:, 1] * 100
    return bulk_predictions, bulk_probability


# Main entry point for Streamlit app
if __name__ == "__main__":
    predict_page()
