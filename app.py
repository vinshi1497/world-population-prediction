import streamlit as st
import pandas as pd
import numpy as np
import joblib


# Load trained model and feature columns
model = joblib.load("best_population_model.pkl")
feature_cols = joblib.load("population_feature_columns.pkl")


# Page configuration
st.set_page_config(
    page_title="World Population Predictor",
    page_icon="🌍",
    layout="centered"
)


# Title
st.title("🌍 World Population Predictor")

st.write(
    "Predict a country's population using demographic and "
    "geographic characteristics."
)


# Input section
st.subheader("Enter Country Information")


density = st.number_input(
    "Population Density (people/km²)",
    min_value=0.0,
    value=100.0
)

land_area = st.number_input(
    "Land Area (km²)",
    min_value=1.0,
    value=100000.0
)

fertility = st.number_input(
    "Fertility Rate",
    min_value=0.0,
    value=2.0
)

median_age = st.number_input(
    "Median Age",
    min_value=0.0,
    max_value=100.0,
    value=30.0
)

urban_population = st.number_input(
    "Urban Population (%)",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

migrants = st.number_input(
    "Net Migrants",
    value=0.0
)

yearly_change = st.number_input(
    "Yearly Population Change (%)",
    value=1.0
)


# Prediction button
if st.button("🌍 Predict Population"):

    input_data = pd.DataFrame(
        [[
            density,
            land_area,
            fertility,
            median_age,
            urban_population,
            migrants,
            yearly_change
        ]],
        columns=feature_cols
    )

    # Predict log population
    predicted_log_population = model.predict(input_data)[0]

    # Convert back from log scale
    predicted_population = np.exp(predicted_log_population)

    # Display result
    st.success(
        f"Predicted Population: {predicted_population:,.0f}"
    )

    st.metric(
        "Estimated Population",
        f"{predicted_population:,.0f}"
    )
interface.launch()
