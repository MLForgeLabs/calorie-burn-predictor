import streamlit as st
import pandas as pd
import joblib

# Set page title and layout
st.set_page_config(page_title="Calorie Burn Predictor", page_icon="💪", layout="centered")

def main():
    # Load the model
    try:
        model = joblib.load('tuned_xgboost_model.pkl')
    except FileNotFoundError:
        st.error("Error: 'tuned_xgboost_model.pkl' not found. Ensure the model file is in the same directory.")
        return
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return

    # App title and description
    st.title("Calorie Burn Predictor 🏃‍♂️")
    st.markdown("""
    Predict calories burned during exercise using an XGBoost model trained on Kaggle data.
    Use the sliders to input your details and get a prediction! Built for @MLForgeLabs! #MLOps #FitnessTech
    """)

    # Input form
    with st.form("prediction_form"):
        st.subheader("Enter Your Details")
        
        # Input fields
        gender = st.selectbox("Gender", ["male", "female"])
        age = st.slider("Age (years)", min_value=0, max_value=120, value=30, step=1)
        height = st.slider("Height (cm)", min_value=50.0, max_value=250.0, value=170.0, step=1.0)
        weight = st.slider("Weight (kg)", min_value=20.0, max_value=300.0, value=70.0, step=1.0)
        duration = st.slider("Exercise Duration (minutes)", min_value=0.0, max_value=300.0, value=30.0, step=1.0)
        heart_rate = st.slider("Heart Rate (bpm)", min_value=30.0, max_value=220.0, value=100.0, step=1.0)
        body_temp = st.slider("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=40.0, step=0.1)
        
        submit_button = st.form_submit_button("Predict Calories Burned")

        if submit_button:
            # Preprocess input
            input_data = {
                'Gender': gender,
                'Age': age,
                'Height': height,
                'Weight': weight,
                'Duration': duration,
                'Heart_Rate': heart_rate,
                'Body_Temp': body_temp
            }
            input_df = pd.DataFrame([input_data])
            input_df['Gender'] = input_df['Gender'].map({'male': 0, 'female': 1})
            
            # Ensure correct feature order
            features = ['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']
            input_df = input_df[features]
            
            # Predict
            try:
                prediction = model.predict(input_df)[0]
                st.success(f"**Predicted Calories Burned: {prediction:.2f} kcal**")
                st.balloons()
            except Exception as e:
                st.error(f"Error during prediction: {e}")

    # MLOps notes
    st.markdown("""
    ### MLOps Notes
    - **Model**: XGBoost, tuned with GridSearchCV (MAE ~1.06, R² ~0.99).
    - **Versioning**: Using pickled model; consider JSON for XGBoost compatibility.
    - **Deployment**: Hosted on Streamlit Cloud, ready for FastAPI API.
    - **Next Steps**: Add MLflow for experiment tracking, DVC for data versioning.
    Check out the code on [GitHub](#) for more! #MLOps @MLForgeLabs
    """)

if __name__ == "__main__":
    main()