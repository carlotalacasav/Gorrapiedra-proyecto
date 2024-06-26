import branca
import folium
import geopandas as gpd
import pandas as pd
import streamlit as st
from folium.features import GeoJsonPopup, GeoJsonTooltip
from streamlit_folium import st_folium

st.write("# GeoJson Popup")

@st.cache_resource
def load_data() -> pd.DataFrame:
    # Load your dataset with bike availability data
    df = pd.read_csv("../full_data.csv")
    return df

@st.cache_resource
def load_geojson() -> gpd.GeoDataFrame:
    geo_df = gpd.read_file("data/locations_data/geo_data/codigos_postales.shp")
    return geo_df

# Load data
df = load_data()
geo_df = load_geojson()
st.write("Data loaded.")

# Ensure the 'post_code' columns are of the same type (string)
df['post_code'] = df['post_code'].astype(str)
geo_df['post_code'] = geo_df['COD_POSTAL'].astype(str)  # Adjust the column name if needed

# Calculate average percentage docks available by postcode
avg_percentage_by_postcode = df.groupby('post_code')['percentage_docks_available'].mean().reset_index()

st.write("Average percentage by postcode:", avg_percentage_by_postcode)

# Merge the GeoDataFrame with the availability data
merged = geo_df.merge(avg_percentage_by_postcode, on='post_code', how='left')

# Debugging: Check the first few rows of the merged data
st.write("Merged data:", merged.head())

# Check if the geometries are valid
if not merged.geometry.is_valid.all():
    merged = merged.buffer(0)

# Re-project the GeoDataFrame to EPSG:3857 for accurate centroid calculation
projected_merged = merged.to_crs(epsg=3857)

# Calculate the centroid for map initialization
centroid = projected_merged.geometry.centroid
mean_lat = centroid.y.mean()
mean_lon = centroid.x.mean()

# Re-project back to geographic CRS (EPSG:4326)
merged = projected_merged.to_crs(epsg=4326)

st.write("Data Preprocessed.")

# Create a folium map centered on the calculated centroid
m = folium.Map(location=[mean_lat, mean_lon], zoom_start=10)

# Create GeoJsonPopup and GeoJsonTooltip
popup = GeoJsonPopup(
    fields=["post_code", "percentage_docks_available"],
    aliases=["Postcode", "Avg % Docks Available"],
    localize=True,
    labels=True,
    style="background-color: yellow;",
)

tooltip = GeoJsonTooltip(
    fields=["post_code", "percentage_docks_available"],
    aliases=["Postcode:", "Avg % Docks Available:"],
    localize=True,
    sticky=False,
    labels=True,
    style="""
        background-color: #F0EFEF;
        border: 2px solid black;
        border-radius: 3px;
        box-shadow: 3px;
    """,
    max_width=800,
)

# Add GeoJson to the map with custom style
folium.GeoJson(
    merged,
    style_function=lambda x: {
        "fillColor": "lightblue" if x['properties'].get('percentage_docks_available') is not None else "transparent",
        "color": "black",
        "fillOpacity": 0.4,
    },
    tooltip=tooltip,
    popup=popup,
).add_to(m)

# Display the map in Streamlit
st_folium(m, width=700, height=500)
