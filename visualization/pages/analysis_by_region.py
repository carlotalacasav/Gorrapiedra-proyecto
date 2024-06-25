import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium
import branca.colormap as cm

@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def get_average_docks(post_code: str) -> float:
    return avg_docks.set_index('post_code').loc[post_code]['percentage_docks_available']

# Create a linear colormap from red to white
colormap = cm.LinearColormap(colors=['red', 'white'], vmin=0, vmax=1)

def get_color(percentage):
    return colormap(percentage)

df = load_data("../full_data.csv")
st.write("Data loaded.")

# Extract unique hours and sort them for the filter
unique_hours = sorted(df['hour'].unique())

# Create a dropdown menu for selecting the hour
selected_hour = st.selectbox('Select Hour', unique_hours)

# Filter the dataframe based on the selected hour
filtered_df = df[df['hour'] == selected_hour]

# Calculate average percentage docks available for each postcode at the selected hour
avg_docks = filtered_df.groupby('post_code').agg({'percentage_docks_available': 'mean', 'lat': 'first', 'lon': 'first'}).reset_index()

st.write(
    "Map showing the average percentage of docks available in different postcodes of Barcelona at different times."
)

# Barcelona coordinates
barcelona_coords = [41.41, 2.25]

st.write("## Barcelona Dock Availability")

#with st.echo(code_location="below"):
# afegim markers al mapa
m = folium.Map(location=barcelona_coords, zoom_start=12)

for row in avg_docks.itertuples():
    color = get_color(row.percentage_docks_available)
    folium.Marker(
        location=[row.lat, row.lon],
        popup=f"Postcode: {row.post_code}<br>Average Docks Available: {row.percentage_docks_available:.2f}%",
        tooltip=f"Postcode: {row.post_code}",
        icon=folium.Icon(color='white', icon_color=color, icon='info-sign')
    ).add_to(m)

st_folium(m, width=1200, height=500)


# REPETEIXO PER DIES DE LA SETMANA
# atres