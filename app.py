import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("house_model.pkl", "rb"))

# App Title
st.title("🏠 House Price Prediction App")

st.write("Enter house details below:")

# User Inputs
area = st.number_input(
    "Area (sq ft)",
    min_value=500,
    max_value=10000,
    value=1500
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

age = st.number_input(
    "House Age (years)",
    min_value=0,
    max_value=50,
    value=5
)

# Prediction Button
if st.button("Predict Price"):

    input_data = pd.DataFrame(
        [[area, bedrooms, age]],
        columns=["Area", "Bedrooms", "Age"]
    )

    prediction = model.predict(input_data)

    st.success(
        f"Estimated House Price: ₹ {prediction[0]:,.0f}"
    )