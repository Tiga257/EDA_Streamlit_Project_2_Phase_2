import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import plotly.graph_objects as go
import plotly.express as px

# Dashboard page
def dashboard_page():
    st.title("Dashboard")

    # Load data
    data = pd.read_csv("data/train_set.csv")

     # Calculate KPIs
    churn_rate = data["Churn"].value_counts(normalize=True)[1] * 100
    avg_tenure = data["Tenure"].mean()
    avg_monthly_charges = data["MonthlyCharges"].mean()
    senior_citizen_ratio = data["SeniorCitizen"].value_counts(normalize=True)[1] * 100
    gender_balance_male = data["Gender"].value_counts(normalize=True)["Male"] * 100
    gender_balance_female = data["Gender"].value_counts(normalize=True)["Female"] * 100

    # Dashboard
    st.title("KPI Dashboard")

    # Data Preview
    st.write("---")
    st.subheader("Data Preview")
    st.dataframe(data.head(10))

    # Row 1
    st.write("---")
    col1, col2, col3 = st.columns(3)
    col1.metric("Churn Rate", f"{churn_rate:.2f}%")
    col2.metric("Average Tenure", f"{avg_tenure:.2f} months")
    col3.metric("Average Monthly Charges", f"$ {avg_monthly_charges:.2f}")

    # Row 2
    col4, col5, col6 = st.columns(3)
    col4.metric("Senior Citizen Ratio", f"{senior_citizen_ratio:.2f}%")
    col5.metric("Gender Balance (Male)", f"{gender_balance_male:.2f}%")
    col6.metric("Gender Balance (Female)", f"{gender_balance_female:.2f}%")

    # Plots
    st.write("---")
    st.subheader("Distributions")

    # Churn Distribution
    col7, col8 = st.columns(2)
    with col7:
        fig, ax = plt.subplots()
        sns.countplot(data["Churn"], ax=ax)
        ax.set_title("Churn Distribution")
        ax.set_xlabel("Churn")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    # Tenure Distribution
    with col8:
        fig, ax = plt.subplots()
        sns.histplot(data["Tenure"], ax=ax, bins=10)
        ax.set_title("Tenure Distribution")
        ax.set_xlabel("Tenure")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    # Monthly Charges Distribution
    st.write("---")
    fig, ax = plt.subplots()
    sns.histplot(data["MonthlyCharges"], ax=ax, bins=10)
    ax.set_title("Monthly Charges Distribution")
    ax.set_xlabel("Monthly Charges")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)



    # Histograms
    st.subheader("Tenure Distribution")
    fig, ax = plt.subplots()
    data["Tenure"].plot.hist(ax=ax)
    ax.set_title("Tenure Distribution")
    ax.set_xlabel("Tenure")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

    # Box Plots
    st.subheader("Monthly Charges Distribution")
    fig, ax = plt.subplots()
    data["MonthlyCharges"].plot.box(ax=ax)
    ax.set_title("Monthly Charges Distribution")
    ax.set_xlabel("Monthly Charges")
    st.pyplot(fig)

    # Density Plots
    st.subheader("Total Charges Distribution")
    fig, ax = plt.subplots()
    sns.kdeplot(data["TotalCharges"], ax=ax)
    ax.set_title("Total Charges Distribution")
    ax.set_xlabel("Total Charges")
    st.pyplot(fig)

    # Bar Charts
    st.subheader("Gender Distribution")
    fig, ax = plt.subplots()
    data["Gender"].value_counts().plot(kind="bar", ax=ax)
    ax.set_title("Gender Distribution")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

    # Pie Charts
    st.subheader("Churn Distribution")
    fig, ax = plt.subplots()
    data["Churn"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
    ax.set_title("Churn Distribution")
    st.pyplot(fig)

    # Count Plots
    st.subheader("Senior Citizen Distribution")
    fig, ax = plt.subplots()
    sns.countplot(data["SeniorCitizen"], ax=ax)
    ax.set_title("Senior Citizen Distribution")
    ax.set_xlabel("Senior Citizen")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)


    st.title("BIVARIATE ANALYSIS")
        # Scatter Plots
    st.subheader("Tenure vs Monthly Charges")
    fig, ax = plt.subplots()
    sns.scatterplot(x="Tenure", y="MonthlyCharges", data=data, ax=ax)
    st.pyplot(fig)

    # Regression Plots
    st.subheader("Tenure vs Monthly Charges Regression")
    fig, ax = plt.subplots()
    sns.regplot(x="Tenure", y="MonthlyCharges", data=data, ax=ax)
    st.pyplot(fig)

    # Box Plots
    st.subheader("Churn vs Monthly Charges")
    fig, ax = plt.subplots()
    sns.boxplot(x="Churn", y="MonthlyCharges", data=data, ax=ax)
    st.pyplot(fig)

    # Violin Plots
    st.subheader("Churn vs Monthly Charges")
    fig, ax = plt.subplots()
    sns.violinplot(x="Churn", y="MonthlyCharges", data=data, ax=ax)
    st.pyplot(fig)

    # Heatmaps
    st.subheader("Gender vs Churn Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(pd.crosstab(data["Gender"], data["Churn"]), ax=ax, annot=True, cmap="coolwarm")
    st.pyplot(fig)

    # Stacked Bar Charts
    st.subheader("Gender vs Churn Stacked Bar Chart")
    fig, ax = plt.subplots()
    pd.crosstab(data["Gender"], data["Churn"]).plot(kind="bar", stacked=True, ax=ax)
    st.pyplot(fig)

    st.title("MULTIVARIATE ANALYSIS")   
        # Pair Plots
    st.subheader("Pair Plot of Numerical Variables")
    fig, ax = plt.subplots()
    sns.pairplot(data[["Tenure", "MonthlyCharges", "TotalCharges"]])
    st.pyplot(fig)

    # 3D Scatter Plots
    st.subheader("3D Scatter Plot of Numerical Variables")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data["Tenure"], data["MonthlyCharges"], data["TotalCharges"])
    st.pyplot(fig)

    # Clustered Bar Charts
    st.subheader("Clustered Bar Chart of Categorical Variables")
    fig, ax = plt.subplots()
    pd.crosstab(data["Gender"], [data["Churn"], data["SeniorCitizen"]]).plot(kind="bar", ax=ax)
    st.pyplot(fig)

    # Sankey Diagrams
    st.subheader("Sankey Diagram of Categorical Variables")
    
    fig = go.Figure(data=[go.Sankey(link = dict(source = [0, 1, 2], target = [1, 2, 0], value = [8, 4, 2]))])
    st.plotly_chart(fig)

    # Parallel Coordinates Plots
    st.subheader("Parallel Coordinates Plot of Mixed Variables")
   
    fig = px.parallel_coordinates(data, color="Churn")
    st.plotly_chart(fig)

    # Radial Plots
    st.subheader("Radial Plot of Mixed Variables")
    import plotly.graph_objects as go
    fig = go.Figure(data=go.Scatterpolar(r=data["MonthlyCharges"], theta=data["Tenure"], fill='toself', name="Customers"))
    st.plotly_chart(fig)

