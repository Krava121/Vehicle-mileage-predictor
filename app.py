import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load("mileage_model.pkl")

st.title("🚗 Vehicle Mileage Predictor")

st.write("Enter vehicle specs below to estimate the mileage (mpg):")

# Input fields
cylinders = st.number_input("Cylinders", min_value=3, max_value=12, value=4)
displacement = st.number_input("Displacement", value=150.0)
horsepower = st.number_input("Horsepower", value=95.0)
weight = st.number_input("Weight", value=2500.0)
acceleration = st.number_input("Acceleration", value=15.0)
year = st.number_input("Model Year (e.g., 70 for 1970)", min_value=70, max_value=83, value=76)
origin = st.selectbox("Origin", options=[1, 2, 3], format_func=lambda x: {1: "USA", 2: "Europe", 3: "Asia"}[x])

# Predict button
if st.button("Predict Mileage"):
    input_data = np.array([[cylinders, displacement, horsepower, weight, acceleration, year, origin]])
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Mileage: {prediction:.2f} mpg")
