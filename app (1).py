import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="Used Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)

# --- Load Pre-trained Model and Columns ---
# Use st.cache_resource to load the model and columns only once
@st.cache_resource
def load_model_and_columns():
    """
    Loads the saved model and column list from .pkl files.
    """
    with open('car_price_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('model_columns.pkl', 'rb') as columns_file:
        columns = pickle.load(columns_file)
    return model, columns

model, model_columns = load_model_and_columns()

# --- Streamlit App UI ---

# Main Title
st.title("🚗 Used Car Price Predictor")
st.markdown("Enter the details of a car to get an estimated selling price. This app uses a pre-trained Random Forest model.")

# Create a sidebar for user inputs
st.sidebar.header("Enter Car Details Here:")

def user_input_features():
    """
    Creates sidebar widgets to get user input and returns a DataFrame.
    """
    year = st.sidebar.number_input("Manufacturing Year", 2000, datetime.now().year, 2015, 1)
    present_price = st.sidebar.slider("Current Showroom Price (in Lakhs)", 0.5, 25.0, 5.0, 0.1)
    kms_driven = st.sidebar.slider("Kilometers Driven", 100, 200000, 35000, 500)
    owner = st.sidebar.selectbox("Number of Previous Owners", [0, 1, 2, 3])
    
    fuel_type = st.sidebar.radio("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.sidebar.radio("Seller Type", ["Dealer", "Individual"])
    transmission = st.sidebar.radio("Transmission Type", ["Manual", "Automatic"])

    # Create a dictionary from the inputs
    data = {
        'Present_Price': present_price,
        'Kms_Driven': kms_driven,
        'Owner': owner,
        'Car_Age': datetime.now().year - year,
        'Fuel_Type_Diesel': 1 if fuel_type == 'Diesel' else 0,
        'Fuel_Type_Petrol': 1 if fuel_type == 'Petrol' else 0,
        'Seller_Type_Individual': 1 if seller_type == 'Individual' else 0,
        'Transmission_Manual': 1 if transmission == 'Manual' else 0
    }
    
    # Convert the dictionary to a pandas DataFrame
    features = pd.DataFrame(data, index=[0])
    
    # Reorder columns to match the model's training order
    # This is a CRITICAL step!
    features = features[model_columns]
    
    return features

# Get user input
input_df = user_input_features()

# Display the user input in the main area
st.subheader("Your Selections:")
st.write(input_df.T.rename(columns={0: 'Values'}))

# Prediction Button and Output
if st.sidebar.button("Predict Price"):
    prediction = model.predict(input_df)
    
    st.success(f"**Predicted Selling Price: ₹ {prediction[0]:,.2f} Lakhs**")
    
st.markdown("---")
st.write("This app uses a Random Forest Regressor to predict used car prices.")