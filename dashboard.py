import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
# from mpl_toolkits.mplot3d import Axes3D

# Dashboard page
def dashboard_page():
    st.title("DASHBOARD")

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
    st.header("KPI Dashboard")

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



    # Set a general aesthetic theme for all plots
    sns.set(style="whitegrid", palette="pastel")

    # Subheading for Churn Analysis
    st.subheader("Churn Analysis")
    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots()
        sns.countplot(x="Churn", data=data, ax=ax, palette="coolwarm")
        ax.set_title("Churn Distribution", color="darkblue", fontsize=15, weight="bold")
        ax.set_xlabel("Churn", color="darkblue")
        ax.set_ylabel("Frequency", color="darkblue")
        st.pyplot(fig)

    with col2:
        # Subheading for Senior Citizen Distribution
        st.subheader("Senior Citizen Distribution")
        fig, ax = plt.subplots()
        sns.countplot(x="SeniorCitizen", data=data, ax=ax, palette="Blues")
        ax.set_title("Senior Citizen Distribution", color="darkblue", fontsize=15, weight="bold")
        ax.set_xlabel("Senior Citizen", color="darkblue")
        ax.set_ylabel("Frequency", color="darkblue")
        st.pyplot(fig)

    # Subheading for Tenure Distribution
    st.subheader("Tenure Analysis")
    col3, col4 = st.columns(2)
    with col3:
        fig, ax = plt.subplots()
        sns.histplot(data["Tenure"], ax=ax, bins=10, color="skyblue", edgecolor="black")
        ax.set_title("Tenure Distribution", color="darkblue", fontsize=15, weight="bold")
        ax.set_xlabel("Tenure", color="darkblue")
        ax.set_ylabel("Frequency", color="darkblue")
        st.pyplot(fig)

    # Subheading for Monthly Charges Analysis
    st.subheader("Monthly Charges Analysis")
    col5, col6 = st.columns(2)
    with col5:
        fig, ax = plt.subplots()
        sns.histplot(data["MonthlyCharges"], ax=ax, bins=10, color="lightcoral", edgecolor="black")
        ax.set_title("Monthly Charges Distribution", color="darkblue", fontsize=15, weight="bold")
        ax.set_xlabel("Monthly Charges", color="darkblue")
        ax.set_ylabel("Frequency", color="darkblue")
        st.pyplot(fig)

    with col6:
        fig, ax = plt.subplots()
        sns.boxplot(x=data["MonthlyCharges"], ax=ax, color="lightgreen")
        ax.set_title("Monthly Charges Box Plot", color="darkblue", fontsize=15, weight="bold")
        ax.set_xlabel("Monthly Charges", color="darkblue")
        st.pyplot(fig)

    # Subheading for Total Charges Density
    st.subheader("Total Charges Analysis")
    fig, ax = plt.subplots()
    sns.kdeplot(data["TotalCharges"], ax=ax, color="purple", shade=True, linewidth=2)
    ax.set_title("Total Charges Density", color="darkblue", fontsize=15, weight="bold")
    ax.set_xlabel("Total Charges", color="darkblue")
    st.pyplot(fig)

    # Subheading for Gender and Churn Distribution
    st.subheader("Demographics Analysis")
    col7, col8 = st.columns(2)
    with col7:
        fig, ax = plt.subplots()
        data["Gender"].value_counts().plot(kind="bar", color=["blue", "orange"], ax=ax)
        ax.set_title("Gender Distribution", color="darkblue", fontsize=15, weight="bold")
        ax.set_xlabel("Gender", color="darkblue")
        ax.set_ylabel("Frequency", color="darkblue")
        st.pyplot(fig)

    with col8:
        fig, ax = plt.subplots()
        data["Churn"].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=["gold", "lightcoral"], ax=ax)
        ax.set_title("Churn Distribution", color="darkblue", fontsize=15, weight="bold")
        st.pyplot(fig)

    


# Sample data (replace with your own DataFrame)
    data = pd.DataFrame({
    'Tenure': [10, 20, 30, 40, 50],
    'MonthlyCharges': [70, 80, 90, 100, 110],
    'TotalCharges': [700, 1600, 2700, 4000, 5500],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Churn': [1, 0, 1, 0, 1],
    'SeniorCitizen': [0, 1, 0, 1, 0]
    })

    st.title("BIVARIATE ANALYSIS")

        # Bubble Plot - Monthly Charges vs Total Charges with Tenure as Bubble Size
    st.subheader("Monthly Charges vs Total Charges (Bubble Plot with Tenure)")
    fig, ax = plt.subplots()
    bubble_plot = ax.scatter(
        x=data["MonthlyCharges"],
        y=data["TotalCharges"],
        s=data["Tenure"] * 10,  # Adjusted size for visualization; change multiplier as needed
        alpha=0.5,
        c=data["Tenure"],
        cmap="viridis",  # Color map for varying colors based on Tenure
        edgecolor="k"
    )
    ax.set_title("Bubble Plot: Monthly Charges vs Total Charges (Bubble Size = Tenure)")
    ax.set_xlabel("Monthly Charges")
    ax.set_ylabel("Total Charges")
    fig.colorbar(bubble_plot, ax=ax, label="Tenure")
    st.pyplot(fig)
    st.markdown("""
    **Interpretation:** This bubble plot shows the relationship between 'Monthly Charges' and 'Total Charges' with bubble size representing 'Tenure'.
    - **Observations**: Larger bubbles indicate customers with longer tenure. This plot helps identify if customers with higher monthly charges tend to accumulate larger total charges, and how tenure influences this.
    """)

    # Regression Plot - Tenure vs Monthly Charges
    st.subheader("Tenure vs Monthly Charges Regression")
    fig, ax = plt.subplots()
    sns.regplot(x="Tenure", y="MonthlyCharges", data=data, ax=ax, scatter_kws={'color':'skyblue', 's':100}, line_kws={'color':'darkblue', 'linewidth':2})
    ax.set_title("Regression Plot: Tenure vs Monthly Charges")
    ax.set_xlabel("Tenure")
    ax.set_ylabel("Monthly Charges")
    st.pyplot(fig)
    st.markdown("""
    **Interpretation:** The regression plot shows the trend line for 'Tenure' and 'Monthly Charges'.
    - **Observations**: A positive slope suggests that monthly charges increase with tenure.
    """)

    # Box Plot - Churn vs Monthly Charges
    st.subheader("Churn vs Monthly Charges")
    fig, ax = plt.subplots()
    sns.boxplot(x="Churn", y="MonthlyCharges", data=data, ax=ax, palette="Set3")
    ax.set_title("Box Plot: Churn vs Monthly Charges")
    st.pyplot(fig)
    st.markdown("""
    **Interpretation:** This box plot shows the distribution of 'Monthly Charges' within churn categories.
    - **Observations**: Compare the range and median of monthly charges for customers who churned vs those who didn’t.
    """)

    # Violin Plot - Churn vs Monthly Charges
    st.subheader("Churn vs Monthly Charges")
    fig, ax = plt.subplots()
    sns.violinplot(x="Churn", y="MonthlyCharges", data=data, ax=ax, palette="muted")
    ax.set_title("Violin Plot: Churn vs Monthly Charges")
    st.pyplot(fig)
    st.markdown("""
    **Interpretation:** The violin plot provides a detailed view of 'Monthly Charges' distributions for each churn status.
    - **Observations**: Look for any skewness or multimodal distributions within each churn group.
    """)

    # Heatmap - Gender vs Churn
    st.subheader("Gender vs Churn Heatmap")
    fig, ax = plt.subplots()
    heat_data = pd.crosstab(data["Gender"], data["Churn"])
    sns.heatmap(heat_data, ax=ax, annot=True, cmap="coolwarm", cbar_kws={'label': 'Count'})
    ax.set_title("Heatmap: Gender vs Churn")
    st.pyplot(fig)
    st.markdown("""
    **Interpretation:** The heatmap shows the counts of churn by gender.
    - **Observations**: Use this to see if churn rates differ significantly between genders.
    """)

    # Stacked Bar Chart - Gender vs Churn
    st.subheader("Gender vs Churn Stacked Bar Chart")
    fig, ax = plt.subplots()
    stacked_bar_data = pd.crosstab(data["Gender"], data["Churn"])
    stacked_bar_data.plot(kind="bar", stacked=True, ax=ax, color=['#A8D8EA', '#FFAA4C'])
    ax.set_title("Stacked Bar Chart: Gender vs Churn")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Count")
    st.pyplot(fig)
    st.markdown("""
    **Interpretation:** The stacked bar chart shows the distribution of churn within each gender.
    - **Observations**: Identify if one gender has a higher churn rate than the other.
    """)


    st.title("MULTIVARIATE ANALYSIS")  
    # Sample data (replace with your own DataFrame)
    data = pd.DataFrame({
        'Tenure': [10, 20, 30, 40, 50],
        'MonthlyCharges': [70, 80, 90, 100, 110],
        'TotalCharges': [700, 1600, 2700, 4000, 5500],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'Churn': [1, 0, 1, 0, 1],
        'SeniorCitizen': [0, 1, 0, 1, 0]
    })

    # Pair Plot of Numerical Variables
    st.subheader("Pair Plot of Numerical Variables")
    sns.set_palette("Set2")  # Set color palette
    pair_plot = sns.pairplot(data[["Tenure", "MonthlyCharges", "TotalCharges"]], diag_kind="kde", kind="scatter", plot_kws={'alpha': 0.7, 's': 50})
    pair_plot.fig.suptitle("Pair Plot of Tenure, Monthly Charges, and Total Charges", y=1.02)
    st.pyplot(pair_plot.fig)

    st.markdown("""
    **Interpretation:** This pair plot allows us to observe the relationships between 'Tenure', 'Monthly Charges', and 'Total Charges'. 
    - **Diagonal**: The KDE plots on the diagonal give insight into the distribution of each variable.
    - **Scatter plots**: Off-diagonal scatter plots show relationships; for example, 'Total Charges' seems to increase with both 'Tenure' and 'Monthly Charges'.
    """)

    # 3D Scatter Plot of Numerical Variables
    st.subheader("3D Scatter Plot of Numerical Variables")
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(data["Tenure"], data["MonthlyCharges"], data["TotalCharges"], c=data["TotalCharges"], cmap="viridis", marker='o', s=50)
    ax.set_xlabel("Tenure")
    ax.set_ylabel("Monthly Charges")
    ax.set_zlabel("Total Charges")
    fig.colorbar(scatter, ax=ax, label="Total Charges")
    st.pyplot(fig)

    st.markdown("""
    **Interpretation:** This 3D scatter plot shows the interaction between 'Tenure', 'Monthly Charges', and 'Total Charges'.
    - **Color scale**: Indicates 'Total Charges' values, which increase as 'Tenure' and 'Monthly Charges' rise.
    - **Trends**: We observe a trend where customers with higher 'Tenure' and 'Monthly Charges' also have higher 'Total Charges'.
    """)

    # Clustered Bar Chart of Categorical Variables
    st.subheader("Clustered Bar Chart of Categorical Variables")
    fig, ax = plt.subplots(figsize=(10, 5))
    clustered_bar = pd.crosstab(data["Gender"], [data["Churn"], data["SeniorCitizen"]])
    clustered_bar.plot(kind="bar", color=['#5A9', '#E33'], ax=ax)
    ax.set_title("Clustered Bar Chart: Gender, Churn, and Senior Citizen")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Count")
    st.pyplot(fig)

    st.markdown("""
    **Interpretation:** This clustered bar chart allows us to examine the distribution of 'Churn' and 'Senior Citizen' status within each gender.
    - **Gender Comparison**: We can analyze differences in churn and senior citizenship between male and female customers.
    """)

    # Sankey Diagram of Categorical Variables
    st.subheader("Sankey Diagram of Categorical Variables")
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15, thickness=20, line=dict(color="black", width=0.5),
            label=["Gender: Male", "Gender: Female", "Churn: Yes", "Churn: No", "Senior Citizen: Yes", "Senior Citizen: No"],
            color=["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A", "#19D3F3"]
        ),
        link=dict(source=[0, 1, 2, 3, 4], target=[2, 3, 4, 5, 3], value=[8, 4, 2, 3, 5])
    )])
    fig.update_layout(title_text="Sankey Diagram: Gender, Churn, and Senior Citizen", font_size=10)
    st.plotly_chart(fig)

    st.markdown("""
    **Interpretation:** This Sankey diagram visualizes flows between categories of gender, churn, and senior citizen status.
    - **Connections**: Flows represent transitions between categories, allowing us to observe the distribution of gender with churn and senior status.
    """)

    # Parallel Coordinates Plot of Mixed Variables
    st.subheader("Parallel Coordinates Plot of Mixed Variables")
    fig = px.parallel_coordinates(
        data, color="Churn", labels={"Tenure": "Tenure", "MonthlyCharges": "Monthly Charges", "TotalCharges": "Total Charges"},
        color_continuous_scale=px.colors.diverging.Tealrose, title="Parallel Coordinates: Tenure, Monthly Charges, Total Charges, Churn"
    )
    st.plotly_chart(fig)

    st.markdown("""
    **Interpretation:** This parallel coordinates plot illustrates the relationship between multiple variables and churn.
    - **Patterns**: Variations in line patterns and color indicate how changes in 'Tenure', 'Monthly Charges', and 'Total Charges' relate to churn.
    """)

    # Radial Plot of Mixed Variables
    st.subheader("Radial Plot of Mixed Variables")
    fig = go.Figure(data=go.Scatterpolar(
        r=data["MonthlyCharges"], theta=data["Tenure"], fill='toself', name="Customers",
        marker=dict(color="lightseagreen")
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, data["MonthlyCharges"].max()])),
        title="Radial Plot: Monthly Charges by Tenure"
    )
    st.plotly_chart(fig)

    st.markdown("""
    **Interpretation:** This radial plot provides a circular representation of 'Monthly Charges' relative to 'Tenure'.
    - **Distribution**: We can see how 'Monthly Charges' vary over the tenure of customers.
    """)



