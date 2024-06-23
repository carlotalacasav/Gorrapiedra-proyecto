import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
import numpy as np
from streamlit_folium import st_folium

st.title("Bicing App")

# Example DataFrame (you can replace this with your actual DataFrame)
data = {
    'year': np.random.randint(2020, 2024, 200),
    'month': np.random.randint(1, 13, 200),
    'day': np.random.randint(1, 32, 200),
    'hour': np.random.randint(0, 24, 200),
    'lat': np.random.uniform(41.35, 41.42, 200),
    'lon': np.random.uniform(2.10, 2.20, 200),
    'capacity': np.random.randint(10, 50, 200),
    'station_id': np.random.randint(1, 100, 200)
}
df = pd.DataFrame(data)

barcelona_map = [41.3851, 2.1734]
map = folium.Map(location=barcelona_map, zoom_start=12)

# Generate random predictions for demonstration
def predict_availability(row):
    return np.random.uniform(0, 100)

heat_data = []

for idx, row in df.iterrows():
    pred = predict_availability(row)
    # Each entry in heat_data is (latitude, longitude, weight)
    heat_data.append([row['lat'], row['lon'], pred])

# Add a button to generate heatmap
if st.button('Generate Heatmap'):
    
    # Add HeatMap layer to the map
    HeatMap(heat_data).add_to(map)
    # Store the map in session state
    st.session_state.heatmap_generated = True

# Visualización del mapa en la aplicación de Streamlit
st_folium(map, width=725, height=500)

# Texto decorativo sobre la aplicación
st.write("""Aquest mapa mostra la predicció dels espais buits de bicicletes a cadascuna de les estacions""")

