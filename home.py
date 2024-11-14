# Save this as home.py
import streamlit as st

def home_page():
    # Title and Header
    st.title('Telco Customer Churn Prediction System')
    st.sidebar.title("Home Section")
    
    # Hero Image
    st.image('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop', 
             caption='Advanced Analytics Dashboard', 
             use_column_width=True)

    # Project Overview with detailed explanation
    st.header('HOME: PROJECT DESCRIPTION')
    st.write('''
    Welcome to our advanced telecommunications customer churn prediction platform. This system leverages 
    machine learning algorithms to identify customers at risk of discontinuing their services, enabling 
    proactive retention strategies.
    ''')

    # Comprehensive Features Section
    st.subheader('Advanced Features')
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('''
        **Predictive Analytics:**
        - Real-time churn probability scoring
        - Customer behavior pattern analysis
        - Risk factor identification
        - Historical trend analysis
        - Automated alert systems
        ''')
        
    with col2:
        st.markdown('''
        **Visualization Tools:**
        - Interactive dashboards
        - Customer segmentation maps
        - Trend analysis graphs
        - Feature importance plots
        - ROC and PR curves
        ''')
    

    # Technical Capabilities
    st.subheader('Technical Specifications')
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('''
        **Machine Learning Models:**
        - Random Forest Classifier
        - XGBoost Algorithm
        - Logistic Regression
        - Support Vector Machines
        - Neural Networks
        ''')
    
    with col2:
        st.markdown(''' 
        **Data Processing Capabilities:**
        - Automated data cleaning
        - Feature engineering
        - Missing value imputation
        - Outlier detection
        - Data normalization
        ''')

    # Implementation Guide
    st.subheader('Implementation Process')
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('''
    1. **Data Integration**
       - Upload customer demographic data
       - Import service usage metrics
       - Connect billing information
       - Sync customer interaction history

    2. **Analysis Configuration**
       - Select relevant features
       - Choose prediction timeframe
       - Set alert thresholds
       - Configure model parameters
        ''')

    with col2:
        st.markdown('''
    3. **Model Deployment**
       - Train selected algorithms
       - Validate model performance
       - Deploy prediction pipeline
       - Monitor accuracy metrics
   
    4. **Results Interpretation**
       - View prediction outcomes
       - Analyze feature importance
       - Export detailed reports
       - Track model performance
    ''')

    # Performance Metrics
    st.subheader('Performance Analytics')
    st.markdown('''
    **Key Metrics Tracked:**
    - Model Accuracy: Precision in identifying at-risk customers
    - F1 Score: Balance between precision and recall
    - ROC-AUC: Overall model discrimination ability
    - Confusion Matrix: Detailed prediction breakdown
    - Feature Importance: Key churn indicators
    ''')

    # System Requirements
    st.subheader('System Requirements')
    st.code('''
    Python >= 3.8
    Memory: 8GB minimum
    Storage: 50GB recommended
    CPU: 4+ cores recommended
    GPU: Optional for neural networks
    ''')

print("Created detailed home.py with comprehensive sections")