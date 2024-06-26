import streamlit as st
from PIL import Image

# Streamlit configuration
st.set_page_config(
    page_title="Data Analysis by Time",
    page_icon="⭐️",
)

st.title("Data Analysis by Locations ⭐️")

# Display plots
results = 'data/results/images/'
st.header("Average Percentage Docks Available and Locations per Post Code")
st.subheader("Docks Available and Places of Interest")
img1 = Image.open(results+"dock_availability_interest.png")
st.image(img1)

st.subheader("Docks Available and Leisure Places")
img2 = Image.open(results+"dock_availability_leisure.png")
st.image(img2)

st.subheader("Docks Available and Bike Lines")
img3 = Image.open(results+"dock_availability_bikelines.png")
st.image(img3)

st.subheader("Docks Available with Bike Lines represented")
img4 = Image.open(results+"dock_availability_concarriles.png")
st.image(img4)