import streamlit as st
from PIL import Image

# Streamlit configuration
st.set_page_config(
    page_title="Data Analysis by Weather",
    page_icon="🍂",
)

st.title("Data Analysis by Weather 🍂")

# Display plots
results = 'data/results/images/'
st.header("Seasonal trends")
img1 = Image.open(results+"seasonal_trends.png")
st.image(img1)

st.header("Impact of Precipitation on Docks Availability")
img2 = Image.open(results+"weather_impact_comparison.png")
st.image(img2)

st.header("Correlation matrix")
img3 = Image.open(results+"correlation_matrix.png")
st.image(img3)