import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium
import geopandas as gpd

@st.cache_data
def generate_data():
    data = {
        'year': np.random.randint(2020, 2024, 1000),
        'month': np.random.randint(1, 13, 1000),
        'day': np.random.randint(1, 32, 1000),
        'hour': np.random.randint(0, 24, 1000),
        'lat': np.random.uniform(41.35, 41.42, 1000),
        'lon': np.random.uniform(2.10, 2.20, 1000),
        'capacity': np.random.randint(10, 50, 1000),
        'station_id': np.random.randint(1, 100, 1000)
    }
    df = pd.DataFrame(data)
    return df

# Generate the dataset
df = generate_data()

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat))

# Streamlit application
st.title('Barcelona Station Capacity Heatmap')

# Station ID filter in the sidebar
station_id = st.sidebar.selectbox('Select Station ID (Optional)', options=[None] + list(df['station_id'].unique()))

# Create the base map
m = folium.Map(location=[41.3851, 2.1734], zoom_start=13)

# Add markers with capacity color gradient for all stations
for index, row in gdf.iterrows():
    folium.CircleMarker(
        location=[row.geometry.y, row.geometry.x],
        radius=7,
        popup=f"Lat: {row.geometry.y}, Lon: {row.geometry.x}, Capacity: {row['capacity']}",
        color='crimson',
        fill=True,
        fill_color='crimson'
    ).add_to(m)

# If a specific station ID is selected, highlight it
if station_id:
    selected_station = gdf[gdf['station_id'] == station_id].iloc[0]
    folium.Marker(
        location=[selected_station.geometry.y, selected_station.geometry.x],
        popup=f"Station ID: {selected_station['station_id']}<br>Lat: {selected_station.geometry.y}<br>Lon: {selected_station.geometry.x}<br>Capacity: {selected_station['capacity']}",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Display the map in Streamlit
st_folium(m, width=700, height=500)
