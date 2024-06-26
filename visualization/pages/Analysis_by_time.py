import streamlit as st
from PIL import Image

# Streamlit configuration
st.set_page_config(
    page_title="Data Analysis by Time",
    page_icon="⌛",
)

st.title("Data Analysis by Time ⌛")

# Display plots
results = 'data/results/images/'
st.header("Average Percentage Docks Available per ...")
st.subheader("Docks Available per Month and Year")
img1 = Image.open(results+"average_percentage_per_month_year.png")
st.image(img1)

st.subheader("Docks Available per Day of the Week")
img2 = Image.open(results+"average_percentage_per_day_of_week.png")
st.image(img2)

st.subheader("Docks Available per Month (All Years)")
img3 = Image.open(results+"average_percentage_per_month.png")
st.image(img3)

st.subheader("Docks Available by Hour and Day of the Week")
img4 = Image.open(results+"average_percentage_by_hour_and_day.png")
st.image(img4)

st.subheader("Docks Available working day vs holiday")
img5 = Image.open(results+"average_percentage_by_holiday.png")
st.image(img5)

st.subheader("Docks Available Weekday vs Weekend")
img6 = Image.open(results+"average_percentage_by_weekend.png")
st.image(img6)