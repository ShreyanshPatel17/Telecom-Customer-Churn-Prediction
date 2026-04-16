def show_churn_prediction():

    import streamlit as st

    from utils.load_models import load_all
    from utils.predict_form import preprocess_input, make_prediction, get_retention_suggestion

    # ------------------ LOAD ------------------
    model, scaler, label_encoders, features = load_all()

    st.markdown("<h1 style='text-align: center; color: white;'>📊 Telecom Customer Churn Prediction</h1>", unsafe_allow_html=True)
    st.caption("Predict & Prevent Churn with ML")

    # ------------------ INPUT SECTION ------------------
    with st.form("prediction_form"):

        st.subheader("🧾 Customer Details")

        col1, col2, col3 = st.columns(3)

        # -------- COLUMN 1 --------
        with col1:
            gender = st.selectbox("Gender", ["Male", "Female"])
            senior = st.selectbox("Senior Citizen", ["No", "Yes"])
            partner = st.selectbox("Partner", ["Yes", "No"])
            dependents = st.selectbox("Dependents", ["Yes", "No"])
            phone = st.selectbox("Phone Service", ["Yes", "No"])

        # -------- COLUMN 2 --------
        with col2:
            lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
            internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
            security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
            backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
            protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])

        # -------- COLUMN 3 --------
        with col3:
            support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
            tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
            movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
            contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
            billing = st.selectbox("Paperless Billing", ["Yes", "No"])

        payment = st.selectbox(
            "Payment Method",
            ["Electronic check", "Mailed check",
             "Bank transfer (automatic)", "Credit card (automatic)"]
        )

        col4, col5, col6 = st.columns(3)

        with col4:
            tenure = st.number_input("Tenure (months)", min_value=1, max_value=100, value=12)
        with col5:
            monthly = st.number_input("Monthly Charges",min_value=0.0,max_value=200.0)
        with col6:
            total = st.number_input("Total Charges",min_value=0.0,max_value=10000.0)

        with col5:
            submit = st.columns(3)[1].form_submit_button("🎯 Predict", use_container_width=True)

    # ------------------ VALIDATION ------------------
    valid = True

    if internet == "No":
        if any(x != "No internet service" for x in [security, backup, protection, support, tv, movies]):
            st.error("Internet disabled → related services must be 'No internet service'")
            valid = False

    if phone == "No" and lines != "No phone service":
        st.error("Phone disabled → lines must be 'No phone service'")
        valid = False

    if total < monthly:
        st.error("Total charges cannot be less than monthly charges")
        valid = False

    # ------------------ PREDICTION ------------------
    if submit and valid:

        input_data = {
            'gender': gender,
            'SeniorCitizen': 1 if senior == "Yes" else 0,
            'Partner': partner,
            'Dependents': dependents,
            'PhoneService': phone,
            'MultipleLines': lines,
            'InternetService': internet,
            'OnlineSecurity': security,
            'OnlineBackup': backup,
            'DeviceProtection': protection,
            'TechSupport': support,
            'StreamingTV': tv,
            'StreamingMovies': movies,
            'Contract': contract,
            'PaperlessBilling': billing,
            'PaymentMethod': payment,
            'tenure': tenure,
            'MonthlyCharges': monthly,
            'TotalCharges': total
        }

        df = preprocess_input(input_data, label_encoders, scaler, features)

        pred, prob = make_prediction(model, df)
        prob = round(prob * 100, 2)

        # ------------------ RESULT ------------------
        st.subheader("🔍 Prediction Result")
        st.metric("Churn Probability", f"{prob}%")

        if prob < 40:
            st.success("🟢 Low Risk")
        elif prob < 70:
            st.warning("🟡 Medium Risk")
        else:
            st.error("🔴 High Risk")

        # ------------------ SUGGESTIONS ------------------
        st.subheader("💡 Recommendations")
        for s in get_retention_suggestion(prob):
            st.write(f"• {s}")


