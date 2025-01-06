import streamlit as st
import joblib

# Load the trained model
model = joblib.load('Diabetes_Prediction_Model.pkl')

# Set the page configuration
st.set_page_config(
    page_title="Diabetes Prediction Site",
    page_icon="🩺",
    layout="wide"
)

# Add a sidebar for navigation
st.sidebar.title("Diabetes Checker")
st.sidebar.image(
    "model_image.webp", caption="Your Health Matters", use_container_width=True
)

# Main page title
st.markdown(
    """
    <h1 style="text-align: center; color: #2B579A;">Diabetes Prediction Site 🩺</h1>
    <p style="text-align: center; font-size: 18px; color: #555555;">Enter your health details below to check your risk of diabetes.</p>
    """,
    unsafe_allow_html=True
)

# Create a form layout for user inputs
with st.form("diabetes_form"):
    st.subheader("Enter Your Details")
    
    # Input fields in two columns
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"])
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        hypertension = st.selectbox("Do you have Hypertension?", ["No", "Yes"])
        heart_disease = st.selectbox("Do you have Heart Disease?", ["No", "Yes"])

    with col2:
        smoking_history = st.selectbox(
            "Smoking History",
            ["Never Smoked", "Former Smoker", "Current Smoker", "Occasional", "Unknown"]
        )
        bmi = st.number_input("Enter your BMI (e.g., 25.4)", format="%.1f")
        HbA1c_level = st.number_input("Enter your HbA1c Level (e.g., 6.5)", format="%.1f")
        blood_glucose_level = st.number_input("Enter your Blood Glucose Level (e.g., 120)", step=1)

    # Submit button
    submitted = st.form_submit_button("Predict")

# When the form is submitted
if submitted:
    # Encode inputs
    gender_encoded = 0 if gender == "Female" else 1
    hypertension_encoded = 0 if hypertension == "No" else 1
    heart_disease_encoded = 0 if heart_disease == "No" else 1
    smoking_history_encoded = {
        "Never Smoked": 0,
        "Former Smoker": 1,
        "Current Smoker": 2,
        "Occasional": 3,
        "Unknown": 4,
    }[smoking_history]

    # Prepare the input for the model
    input_data = [
        [
            gender_encoded,
            age,
            hypertension_encoded,
            heart_disease_encoded,
            smoking_history_encoded,
            bmi,
            HbA1c_level,
            blood_glucose_level,
        ]
    ]

    # Make the prediction
    try:
        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)[0][1]  # Probability of diabetes

        # Display results
        if prediction[0] == 1:
            st.markdown(
                f"""
                <div style="background-color: #FFD1D1; padding: 10px; border-radius: 5px; border: 1px solid #FF0000;">
                    <h3 style="text-align: center; color: #FF0000;">High Risk of Diabetes</h3>
                    <p style="text-align: center; font-size: 18px; color: #800000;">Probability: {probability:.2f}</p>
                </div>
                """,
                unsafe_allow_html=True,
            ) 
        else:
            st.markdown(
                f"""
                <div style="background-color: #DFF6DD; padding: 10px; border-radius: 5px; border: 1px solid #4CAF50;">
                    <h3 style="text-align: center; color: #388E3C;">Low Risk of Diabetes</h3>
                    <p style="text-align: center; font-size: 18px; color: #2E7D32;">Probability: {probability:.2f}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer
st.sidebar.markdown(
    """
    ---
    **Powered by KANI_Healthcare.AI**  
    Contact us: [KANI_Healthcare@gmail.com](mailto:KANI_Healthcare@gmail.com)
    """
)
