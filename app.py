import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
model = pickle.load(open('trained_model.sav', 'rb'))


st.title("Obesity Category Prediction App")

st.markdown("Enter health/lifestyle details to predict **Obesity Category**")


age = st.number_input("Age", min_value=1, max_value=120, step=1)
gender = st.selectbox("Gender", ["Male", "Female"])
height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1)
physical_activity = st.number_input("Physical Activity Level", min_value=0, max_value=10, value=2)


gender_male = 1 if gender == "Male" else 0


input_data = pd.DataFrame({
    'Age': [age],
    'Height': [height],
    'Weight': [weight],
    'BMI': [bmi],
    'PhysicalActivityLevel': [physical_activity],
    'Gender_Male': [gender_male]})


if st.button("Predict"):
    prediction = model.predict(input_data)[0]

    mapping = {0: "Underweight", 1: "Normal weight", 2: "Overweight", 3: "Obese"}
    st.success(f"Predicted Category: **{mapping[prediction]}**")
