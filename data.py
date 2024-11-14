import streamlit as st
import pandas as pd

def data_page():
    # Page title and sidebar introduction
    st.title("DATA SECTION")
    st.sidebar.title("Data Section")
    st.sidebar.write(
        '''View of the data used in the application, 
                     enabling users to explore, filter, and download data 
                     for further analysis.
                     ''')
    
    # Descriptions for columns
    columns_description = {
        "Gender": "Whether the customer is male or female",
        "SeniorCitizen": "Whether the customer is a senior citizen or not",
        "Partner": "Whether the customer has a partner (Yes, No)",
        "Dependents": "Whether the customer has dependents (Yes, No)",
        "Tenure": "Months the customer has been with the company",
        "Phone Service": "Whether the customer has phone service (Yes, No)",
        "MultipleLines": "Whether the customer has multiple lines",
        "InternetService": "Customer's internet provider (DSL, Fiber Optic, No)",
        "OnlineSecurity": "Whether the customer has online security (Yes, No, No Internet)",
        "OnlineBackup": "Whether the customer has online backup (Yes, No, No Internet)",
        "DeviceProtection": "Whether the customer has device protection (Yes, No, No Internet)",
        "TechSupport": "Whether the customer has tech support (Yes, No, No Internet)",
        "StreamingTV": "Whether the customer has streaming TV (Yes, No, No Internet)",
        "StreamingMovies": "Whether the customer has streaming movies (Yes, No, No Internet)",
        "Contract": "The contract term (Month-to-Month, One year, Two year)",
        "PaperlessBilling": "Whether the customer has paperless billing (Yes, No)",
        "Payment Method": "The payment method (Electronic check, Mailed check, Bank transfer, Credit card)",
        "MonthlyCharges": "Monthly amount charged to the customer",
        "TotalCharges": "Total amount charged to the customer",
        "Churn": "Whether the customer churned (Yes, No)"
    }

    # Load dataset (add correct path to your CSV file)
    dataset_path = "data/train_set.csv"
    try:
        data = pd.read_csv(dataset_path)
    except FileNotFoundError:
        st.error(f"Dataset not found at path: {dataset_path}")
        return
    
    # Column selection for descriptions and data filtering
    col1, col2 = st.columns(2)

    with col1:
        # Show description for selected column
        selected_column = st.selectbox(
            "Select a column to view its description:",
            list(columns_description.keys())
        )
        st.write(f"**{selected_column}**: {columns_description[selected_column]}")

    with col2:
        # Filter and display data based on type selection
        data_type = st.selectbox("Select Data Type to Display", ["All", "Numerical", "Categorical"])
        
        if data_type == "Numerical":
            filtered_data = data.select_dtypes(include=["number"])
        elif data_type == "Categorical":
            filtered_data = data.select_dtypes(include=["object", "category"])
        else:
            filtered_data = data

        st.write("### Filtered Data")
        st.write(filtered_data)
    
    # Display full dataset in an expandable section
    with st.expander("View Full Dataset"):
        st.dataframe(data)

    # Summary statistics for quick insights
    st.write("### Dataset Summary")
    st.write(data.describe(include="all"))

