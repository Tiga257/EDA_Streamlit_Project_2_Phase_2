import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def dashboard_page():
    st.title("Customer Churn Dashboard Page")

# load the data
    data =pd.read_csv("data/traindata.csv")

    st.header("Data Overview")
    st.write("Here is a quick summary of the dataset")
    st.dataframe(data.head())

     # Calculate KPIs
    total_customers = len(data)
    churn_rate = round((data['Churn'].value_counts().iloc[1] / total_customers) * 100, 2)
    avg_tenure = round(data['tenure'].mean(), 2)

    # Display KPIs
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Customers", total_customers)
    with col2:
        st.metric("Churn Rate", f"{churn_rate}%")
    with col3:
        st.metric("Average Tenure", f"{avg_tenure} months")

    st.subheader("Interactive Visualization")

        # Selectbox for variable selection
    variable = st.selectbox("Select a variable", options=["tenure", "MonthlyCharges", "TotalCharges"])

   # Create an interactive scatter plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=variable, y="TotalCharges", hue="Churn", data=data, palette="coolwarm")
    plt.title(f"Total Charges vs. {variable} by Churn Status")
    st.pyplot(plt)

# do a correlation heatmap
    # heat map Tenure vs Totalcharges
    st.subheader("Correlation Heatmap")
    corr= data[["tenure", "MonthlyCharges"]].corr()
    plt.figure(figsize =(10, 6))
    sns.heatmap(corr, annot =True, cmap="coolwarm")
    st.pyplot(plt)

     #violinplot churn vs totalcharges
    st.subheader("Total Charges vs. Tenure (Churned vs. Non-Churned)")
    plt.figure(figsize=(10, 6))
    sns.violinplot(x="Churn", y="TotalCharges", hue="Churn", data=data, split=True)
    plt.title("Total Charges vs. Tenure by Churn Status")
    plt.xlabel("Tenure (Months)")
    plt.ylabel("Total Charges")
    st.pyplot(plt)

    # countplot internet service
    st.subheader("Internet Service")
    plt.figure(figsize=(8,5))
    sns.countplot(x="InternetService", data=data, hue ="InternetService", palette="viridis",legend=False )
    plt.title("Distribution of Internet Service Types")
    plt.xlabel("Internet Service")
    plt.ylabel("Count")
    st.pyplot(plt)

    #correlation matrix heatmap
    st.subheader("Correlation Matrix")
    plt.figure(figsize=(10, 8))
    sns.heatmap(data[['tenure', 'MonthlyCharges', 'TotalCharges']].corr(), annot=True, cmap="YlGnBu")
    plt.title("Correlation Matrix of Key Features")
    st.pyplot(plt)

    #scatterplot tenure vs monthlycharges
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="tenure", y="MonthlyCharges", hue="Churn", data=data, palette="coolwarm")
    plt.title("Monthly Charges vs. Tenure by Churn Status")
    plt.xlabel("Tenure (Months)")
    plt.ylabel("Monthly Charges")
    st.pyplot(plt)

    #boxplot tenure vs contract
    st.subheader("Tenure by Contract Type")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="Contract", y="tenure", data=data, hue="Contract", palette="coolwarm", dodge=False)
    plt.title("Tenure Distribution by Contract Type")
    plt.xlabel("Contract Type")
    plt.ylabel("Tenure (Months)")
    st.pyplot(plt)