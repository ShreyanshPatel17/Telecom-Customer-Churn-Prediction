def show_model_workflow():

    import streamlit as st

    # ------------------ CUSTOM CSS ------------------
    st.markdown("""
    <style>

    /* ===== MAIN TITLE (SPECIAL) ===== */
    .main-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #ff512f, #dd2476, #ff6a00, #b06ab3);
        background-size: 300% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientMove 4s linear infinite, fadeInDown 1.2s ease;
        margin-bottom: 20px;
    }

    @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }

    @keyframes fadeInDown {
        0% { opacity: 0; transform: translateY(-40px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    /* ===== SECTION CARDS ===== */
    .card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        transition: 0.3s;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.4);
    }

    /* ===== SECTION TITLES ===== */
    .section-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #38f9d7;
        margin-bottom: 10px;
    }

    /* ===== TEXT ===== */
    .content-text {
        font-size: 1.1rem;
        color: #e5e7eb;
        line-height: 1.8;
        letter-spacing: 0.3px;
    }

    </style>
    """, unsafe_allow_html=True)

    # ------------------ TITLE ------------------
    st.markdown("<div class='main-title'>⚙️ Workflow of Churn Prediction Model</div>", unsafe_allow_html=True)

    # ------------------ OVERVIEW ------------------
    st.markdown("""
    <div class='card'>
        <div class='section-title'>📊 Project Overview</div>
        <div class='content-text'>
        This project predicts whether a telecom customer is likely to churn (leave the service)
        based on customer behavior, services used, and billing information.
        <br><br>
        The primary objective of this project is to:
        <br><br>
        • Identify customers who are likely to churn<br>
        • Analyze patterns and factors influencing churn<br>
        • Build a predictive machine learning model<br>
        • Help businesses take proactive retention actions<br>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ------------------ DATA ------------------
    st.markdown("""
    <div class='card'>
        <div class='section-title'>📁 Dataset Information</div>
        <div class='content-text'>
        The dataset includes:
        <br><br>
        • Demographic details (Gender, Senior Citizen)<br>
        • Account details (Tenure, Contract Type)<br>
        • Services used (Internet, Streaming, Security)<br>
        • Billing details (Monthly & Total Charges)
        <br><br>
        Target variable:
        <br>
        <b>Churn → Whether customer leaves or stays</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ------------------ EDA ------------------
    st.markdown("""
    <div class='card'>
        <div class='section-title'>🔍 Exploratory Data Analysis (EDA)</div>
        <div class='content-text'>
        EDA is performed to understand patterns, relationships, and trends in the data.
        <br><br>
        <b>📈 Key Analysis Performed:</b><br>
        • Distribution of churn vs non-churn customers<br>
        • Churn rate based on contract type, tenure, monthly charges, and services used
        <br><br>
        <b>📊 Insights:</b><br>
        • Customers with month-to-month contracts churn more<br>
        • Higher monthly charges increase churn probability<br>
        • Long tenure customers are more loyal<br>
        • Lack of tech support & security increases churn
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ------------------ PREPROCESSING ------------------
    st.markdown("""
    <div class='card'>
        <div class='section-title'>🧹 Data Preprocessing</div>
        <div class='content-text'>
        Data preprocessing ensures the dataset is clean and suitable for model training.
        <br><br>
        <b>🔧 Steps Performed:</b><br>
        ✔ Handling Missing Values<br>
        • Converted TotalCharges to numeric<br>
        • Removed/imputed missing values
        <br><br>
        ✔ Encoding Categorical Variables<br>
        • Applied Label Encoding<br>
        • Converted categorical features to numeric
        <br><br>
        ✔ Feature Scaling<br>
        • Applied StandardScaler for normalization
        <br><br>
        ✔ Outlier Handling<br>
        • Detected using IQR and visualization<br>
        • Removed/capped extreme values
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ------------------ IMBALANCED DATA ------------------
    st.markdown("""
    <div class='card'>
        <div class='section-title'>⚖️ Handling Imbalanced Data</div>
        <div class='content-text'>
        Churn datasets are usually imbalanced with fewer churn cases.
        <br><br>
        <b>✅ Technique Used:</b><br>
        SMOTE (Synthetic Minority Over-sampling Technique)
        <br><br>
        <b>📌 Purpose:</b><br>
        • Generate synthetic churn samples<br>
        • Balance dataset for better learning
        <br><br>
        <b>📊 Result:</b><br>
        • Improved recall for churn class<br>
        • Reduced model bias
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ------------------ FEATURE ENGINEERING ------------------
    st.markdown("""
    <div class='card'>
        <div class='section-title'>🧠 Feature Engineering</div>
        <div class='content-text'>
        Transformations applied to enhance model performance:
        <br><br>
        • Conversion of categorical variables<br>
        • Feature selection based on importance<br>
        • Removal of redundant or low-impact features
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ------------------ MODEL BUILDING ------------------
    st.markdown("""
    <div class='card'>
        <div class='section-title'>🤖 Model Building</div>
        <div class='content-text'>
        Multiple machine learning models were trained and compared:
        <br><br>
        <b>🔹 Logistic Regression</b><br>
        • Linear classification model<br>
        • Outputs churn probability
        <br><br>
        <b>🔹 Decision Tree</b><br>
        • Rule-based model<br>
        • Easy to interpret but may overfit
        <br><br>
        <b>🔹 Random Forest</b><br>
        • Ensemble of decision trees<br>
        • Reduces overfitting and improves accuracy
        <br><br>
        <b>🔹 K-Nearest Neighbors</b><br>
        • Based on nearest data points<br>
        • Sensitive to scaling
        <br><br>
        <b>🔹 Support Vector Machine</b><br>
        • Finds optimal boundary<br>
        • Effective in high-dimensional space
        <br><br>
        <b>🔹 XGBoost</b><br>
        • Advanced boosting algorithm<br>
        • High performance and efficiency
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ------------------ MODEL EVALUATION ------------------
    st.markdown("""
    <div class='card'>
        <div class='section-title'>📊 Model Evaluation</div>
        <div class='content-text'>
        Models were evaluated using:
        <br><br>
        <b>📈 Metrics Used:</b><br>
        • Accuracy<br>
        • Precision<br>
        • Recall<br>
        • F1-Score
        <br><br>
        <b>📊 Formula:</b><br>
        Accuracy = (TP + TN) / (TP + TN + FP + FN)
        <br><br>
        <b>📉 Observations:</b><br>
        • Tree-based models performed better<br>
        • XGBoost & Random Forest achieved highest accuracy<br>
        • SMOTE improved recall significantly
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ------------------ ENSEMBLE ------------------
    st.markdown("""
    <div class='card'>
        <div class='section-title'>🧩 Ensemble Learning</div>
        <div class='content-text'>
        To improve performance, Voting Classifier was used.
        <br><br>
        <b>📌 Concept:</b><br>
        • Combines multiple model predictions<br>
        • Uses weighted voting
        <br><br>
        <b>📊 Benefits:</b><br>
        • Improved accuracy<br>
        • Reduced variance and bias
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ------------------ HYPERPARAMETER ------------------
    st.markdown("""
    <div class='card'>
        <div class='section-title'>⚙️ Hyperparameter Optimization</div>
        <div class='content-text'>
        GridSearchCV was used for tuning:
        <br><br>
        • Model parameters<br>
        • Voting classifier weights<br>
        • Algorithm-specific hyperparameters
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ------------------ MODEL SAVING ------------------
    st.markdown("""
    <div class='card'>
        <div class='section-title'>💾 Model Saving</div>
        <div class='content-text'>
        Models were saved using Joblib.
        <br><br>
        <b>📌 Purpose:</b><br>
        • Avoid retraining<br>
        • Enable deployment<br>
        • Faster predictions
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ------------------ FINAL WORKFLOW ------------------
    st.markdown("""
    <div class='card'>
        <div class='section-title'>🔮 Prediction Workflow</div>
        <div class='content-text'>
        <b>🔄 Step-by-Step Flow:</b>
        <br><br>
        1. User inputs customer details<br>
        2. Data preprocessing is applied<br>
        3. Features are scaled and encoded<br>
        4. Model predicts churn probability
        <br><br>
        <b>📊 Output:</b><br>
        • Churn / No Churn<br>
        • Confidence Score
        <br><br>
        <b>🎯 Risk Levels:</b><br>
        🟢 Low Risk<br>
        🟡 Moderate Risk<br>
        🔴 High Risk
        </div>
    </div>
    """, unsafe_allow_html=True)

















