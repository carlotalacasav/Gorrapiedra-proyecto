import streamlit as st
from PIL import Image

# Streamlit configuration
st.set_page_config(
    page_title="Data Analysis by Capacity",
    page_icon="🔋",
)

st.title("Data Analysis by Capacity 🔋")

# Display plots
results = 'data/results/images/'
st.header("Average Percentage Docks Availability per Capacity")
img1 = Image.open(results+"capacity.png")
st.image(img1)

st.header("Average Capacity over Time")
img2 = Image.open(results+'average_capacity_daily.png')
st.image(img2)