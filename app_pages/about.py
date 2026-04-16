from turtle import st


def view_about():

    import streamlit as st  

    # ------------------ CUSTOM CSS ------------------
    st.markdown("""
            <style>

            /* ===== MAIN TITLE ===== */
            .main-title {
                text-align: center;
                font-size: 2.8rem;
                font-weight: 800;
                background: linear-gradient(90deg, #ff512f, #dd2476, #ff6a00, #b06ab3);
                background-size: 300% auto;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: gradientMove 4s linear infinite, fadeInDown 1.2s ease;
                margin-bottom: 5px;
            }

            /* ===== SUB TITLE ===== */
            .sub-title {
                text-align: center;
                font-size: 1.3rem;
                color: #9ca3af;
                margin-bottom: 25px;
                animation: fadeIn 2s ease;
            }

            @keyframes gradientMove {
                0% { background-position: 0% 50%; }
                100% { background-position: 100% 50%; }
            }

            @keyframes fadeInDown {
                0% { opacity: 0; transform: translateY(-40px); }
                100% { opacity: 1; transform: translateY(0); }
            }

            @keyframes fadeIn {
                0% { opacity: 0; }
                100% { opacity: 1; }
            }

            /* ===== CARDS ===== */
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

            /* ===== TITLES ===== */
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
    st.markdown("<div class='main-title'>⚙️ Customer Churn Prediction System</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>About the Application</div>", unsafe_allow_html=True)

    # ------------------ OVERVIEW ------------------
    st.markdown("""
            <div class='card'>
                <div class='section-title'>📊 Application Overview</div>
                <div class='content-text'>
                This application is a Machine Learning-based Customer Churn Prediction System designed to identify customers who are likely to discontinue telecom services.
                <br>
                It analyzes customer demographics, service usage patterns, and billing information to generate accurate predictions.
                <br>
                The system helps businesses understand customer behavior and take proactive steps to improve retention, reduce churn rate, and enhance customer satisfaction.
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ------------------ TECHNOLOGIES ------------------
    st.markdown("""
            <div class='card'>
                <div class='section-title'>🧰 Technologies Used</div>
                <div class='content-text'>
                <b>💻 Programming & Development:</b><br>
                • Python<br>
                • Streamlit
                <br>
                <b>📊 Data Analysis & Visualization:</b><br>
                • Pandas<br>
                • NumPy<br>
                • Matplotlib<br>
                • Seaborn
                <br>
                <b>🤖 Machine Learning:</b><br>
                • Scikit-learn<br>
                • XGBoost
                <br>
                <b>⚙️ Model Handling:</b><br>
                • Joblib
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ------------------ ML SYSTEM ------------------
    st.markdown("""
            <div class='card'>
                <div class='section-title'>🧠 ML Behind the System</div>
                <div class='content-text'>
                The system uses multiple Machine Learning algorithms to ensure accurate predictions:
                <br>
                • Logistic Regression<br>
                • Decision Tree<br>
                • Random Forest<br>
                • Support Vector Machine (SVM)<br>
                • K-Nearest Neighbors (KNN)<br>
                • XGBoost
                <br><br>
                <b>Ensemble Technique:</b><br>
                • Voting Classifier combines predictions from multiple models<br>
                • Uses weighted voting for final output
                <br><br>
                This approach improves accuracy, stability, and reliability of predictions.
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ------------------ FEATURES ------------------
    st.markdown("""
            <div class='card'>
                <div class='section-title'>✨ Key Features</div>
                <div class='content-text'>
                • Real-time churn prediction<br>
                • Risk categorization (Low, Moderate, High)<br>
                • Machine Learning-powered insights<br>
                • Handles imbalanced data using SMOTE<br>
                • High accuracy using ensemble learning<br>
                • User-friendly interface with Streamlit
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ------------------ ARCHITECTURE ------------------
    st.markdown("""
            <div class='card'>
                <div class='section-title'>🧩 System Architecture</div>
                <div class='content-text'>
                User Input -→  Data Preprocessing -→  Feature Transformation  -→  ML Models  -→  Voting Classifier  -→  Prediction Output
                <br><br>
                The system follows a structured pipeline ensuring consistency and efficient prediction.
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ------------------ USE CASES ------------------
    st.markdown("""
            <div class='card'>
                <div class='section-title'>💼 Business Use Cases</div>
                <div class='content-text'>
                • Telecom companies to reduce churn<br>
                • Subscription-based platforms (OTT, SaaS)<br>
                • Banking & financial services<br>
                • E-commerce platforms
                <br><br>
                Helps organizations identify high-risk customers and take preventive actions.
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ------------------ SUMMARY ------------------
    st.markdown("""
            <div class='card'>
                <div class='section-title'>🚀 Summary</div>
                <div class='content-text'>
                This application demonstrates how Machine Learning can solve real-world business problems.
                <br>
                By combining data preprocessing, multiple ML models, and ensemble techniques, the system delivers accurate predictions and valuable insights.
                <br>
                It enables organizations to make data-driven decisions, reduce churn, and improve long-term growth.
                </div>
            </div>
            """, unsafe_allow_html=True)






    