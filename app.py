import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("house_price_model.pkl")


# Page settings
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠"
)


# Title
st.title("🏠 House Price Prediction")
st.write("Enter the house details to predict the estimated price.")


# House details

area = st.number_input(
    "Area (sq ft)",
    min_value=300,
    max_value=4000,
    value=1000
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=5,
    value=2
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=5,
    value=2
)

floors = st.number_input(
    "Floors",
    min_value=1,
    max_value=4,
    value=1
)

age = st.number_input(
    "House Age (Years)",
    min_value=0,
    max_value=30,
    value=5
)

parking = st.number_input(
    "Parking Spaces",
    min_value=0,
    max_value=3,
    value=1
)

location = st.selectbox(
    "City",
    [
        "Mumbai",
        "Pune",
        "Nashik",
        "Nagpur",
        "Aurangabad",
        "Kolhapur",
        "Solapur",
        "Sangli",
        "Satara",
        "Amravati",
        "Nanded",
        "Jalgaon",
        "Ahmednagar",
        "Latur",
        "Beed"
    ]
)

furnished = st.selectbox(
    "Furnished",
    [
        "Unfurnished",
        "Semi-Furnished",
        "Furnished"
    ]
)


# Prediction button

if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "Area": [area],
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Floors": [floors],
        "Age": [age],
        "Parking": [parking],
        "Location": [location],
        "Furnished": [furnished]
    })


    # Predict price
    prediction = model.predict(input_data)[0]


    # Display result
    st.success(
        f"🏠 Estimated House Price: ₹ {prediction:.2f} Lakhs"
    )
    st.balloons()