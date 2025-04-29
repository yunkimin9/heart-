import os
import pickle
import streamlit as st
import numpy as np

model_filename = "C:/Users/Asus/OneDrive/Desktop/heart_disease_model.sav"
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

st.title('Heart Disease Prediction App')
st.write("Enter the following details to check for heart disease risk:")

age = st.number_input('Age', min_value=20, max_value=100, value=50)
sex = st.selectbox('Sex (0: Female, 1: Male)', [0, 1])
cpt = st.selectbox('Chest Pain Type (0-3)', [0, 1, 2, 3])
trestbps = st.number_input('Resting Blood Pressure', min_value=80, max_value=200, value=120)
chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=100, max_value=400, value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (1: Yes, 0: No)', [0, 1])
restecg = st.selectbox('Resting ECG Results (0-2)', [0, 1, 2])
thalach = st.number_input('Max Heart Rate Achieved', min_value=60, max_value=220, value=150)
exang = st.selectbox('Exercise Induced Angina (0: No angina during exercise, 1: Angina present during exercise)', [0, 1])
oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=6.0, value=1.0)
slope = st.selectbox('Slope of Peak Exercise ST Segment (0: Upsloping, 1: Flat , 2: Downsloping )', [0, 1, 2])
ca = st.selectbox('Number of Major Vessels (0-4)', [0, 1, 2, 3, 4])
thal = st.selectbox('Thalassemia (genetic blood disorder) (0: No thalassemia, 1: Normal blood flow , 2:Fixed defect (permanent damage in heart) , 3: Reversible defect (temporary blood flow issues))', [0,1,2,3])

if st.button('Predict'):
    if model:
        try:
            input_data = np.array([[age, sex, cpt, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            prediction = model.predict(input_data)
            
            if prediction[0] == 1:
                st.success('The person does NOT have heart disease. ✅')
            else:
                st.error('The person has heart disease. ❌')
                if slope >= 1 or ca > 1 or thal > 1:
                    st.warning("Your results indicate potential risk factors for heart disease. It is highly recommended that you consult a doctor for a professional evaluation.")
        except Exception as e:
            st.error(f"Error making prediction: {e}")
    else:
        st.warning("Please upload a valid model file before predicting.") 
