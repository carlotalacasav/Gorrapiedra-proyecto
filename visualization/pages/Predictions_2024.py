import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium
import branca.colormap as cm
from folium.plugins import HeatMap
from PIL import Image
from streamlit_folium import folium_static


@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


st.set_page_config(
    page_title="Predictions 2024",
    page_icon="🔮",
    layout="wide"
)

st.title("Predictions 2024 🔮")


### code to join the 2024 predictions with the 2024 dataset

y = load_data("../submision_20_128dnn.csv")
df = load_data("../full_data_2024.csv")

#df = pd.merge(x, y[['date', 'percentage_docks_available']], on='date', how='left')
df['percentage_docks_available'] = y['percentage_docks_available']


st.write("Data from 2024 loaded. MSE = 0.1")

# Barcelona coordinates
barcelona_coords = [41.41, 2.25]


avg_docks_hour = df.groupby('post_code').agg({
    'percentage_docks_available': 'mean',
    'lat': 'first',
    'lon': 'first'
}).reset_index()

st.write("## Barcelona Dock Availability ")
st.write(
    "Map showing the average predicted percentage of docks available in different postcodes of Barcelona at different times."
)

def get_gradient_color(percentage):
    col = 1-percentage
    red = int(255)
    green = int(255 * col)
    blue = int(255 * col)
    return f'#{red:02x}{green:02x}{blue:02x}'

m = folium.Map(location=barcelona_coords, zoom_start=12)

for row in avg_docks_hour.itertuples():
    color = get_gradient_color(row.percentage_docks_available)
    folium.Marker(
        location=[row.lat, row.lon],
        popup=(
            f"Postcode: {row.post_code}<br>"
            f"Predicted Avg Docks Available: {row.percentage_docks_available:.2f}%"
        ),
        tooltip=f"Postcode: {row.post_code}",
        icon=folium.Icon(color='white', icon_color=color, icon='info-sign')
    ).add_to(m)

st_folium(m, width=1200, height=500)

# Heatmap de disponibilitat per la hora, el dia i mes
unique_hours = sorted(df['hour'].unique())
unique_days = sorted(df['day'].unique())

selected_hour = st.selectbox('Select Hour', unique_hours)
selected_day = st.selectbox('Select Day', unique_days)
selected_month = st.selectbox('Select Month', range(1, 4))

# filtrem el df per les dades seleccionades

filtered_df = df[(df['hour'] == selected_hour) & (df['day'] == selected_day) & (df['month'] == selected_month)]

avg_docks = filtered_df.groupby('post_code').agg({'percentage_docks_available': 'mean', 'lat': 'first', 'lon': 'first'}).reset_index()

st.write("# Heatmap of the prediction for 2024")
st.write(
    "Heatmap showing the prediction of the percentage of docks available in different postcodes of Barcelona at a given hour, day and month for 2024."
)


m_heatmap = folium.Map(location=barcelona_coords, zoom_start=12)
heat_data = [[row['lat'], row['lon'], row['percentage_docks_available']] for index, row in avg_docks.iterrows()]
#HeatMap(heat_data, min_opacity=0.2, max_zoom=18, radius=15, blur=15).add_to(m_heatmap)

for index, row in avg_docks.iterrows():
    percentage = row['percentage_docks_available']
    circle_color = 'blue'  # Default color
    if percentage <= 0.4:
        circle_color = 'blue'
    elif 0.4 < percentage <= 0.5:
        circle_color = 'lime'
    elif 0.5 < percentage <= 0.6:
        circle_color = 'green'
    elif 0.6 < percentage <= 0.7:
        circle_color = 'pink'
    else:
        circle_color = 'red'

    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=8,
        fill=True,
        color=circle_color,
        fill_color=circle_color,
        fill_opacity=0.7,
        tooltip=f"{percentage:.2f}%",  
        popup=f"{percentage:.2f}%",  
        icon=folium.DivIcon(html=f"<div style='text-align:center; font-size:10pt; background-color:transparent'>{percentage:.2f}%</div>")
    ).add_to(m_heatmap)

folium_static(m_heatmap)

#st_folium(m_heatmap, width=1200, height=500)

st.write("# Average percentage by hour and day")
st.write(
    "Heatmap showing the prediction of the average percentage of docks available by hour and day -  2024."
)

results = 'data/results/images/2024/'
st.header("Average Percentage Docks Available per ...")
st.subheader("Docks Available per Hour and Day")
img1 = Image.open(results+"average_percentage_by_hour_and_day.png")
st.image(img1)