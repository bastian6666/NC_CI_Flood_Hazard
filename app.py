import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")

def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return html_content

# Set up the page title
st.title('Flood Risk Assessment for Critical Infrastructure Using DEM and Landsat Data in North Carolina')

# Directory containing your HTML files for maps
map_directory = '.'

# Path to your single chart HTML file
chart_file_path = 'chart/chart.html'

# List all HTML files in the maps directory and remove the '.html' extension for display
map_files = [f[:-5] for f in os.listdir(map_directory) if f.endswith('.html')]

# Dropdown menu for selecting the map
selected_map = st.selectbox('Choose a map:', map_files)

# Append '.html' back to the selected map for file loading
selected_map_file = selected_map + ".html"

# Load the always-displayed chart
chart_html = load_html(chart_file_path)

# Use Streamlit's columns to specify more precise widths
col1, col2 = st.columns((0.45, 0.55))  # Adjust these ratios as needed

with col1:
    st.header("Map")
    map_html = load_html(os.path.join(map_directory, selected_map_file))
    components.html(map_html, height=600, scrolling=True)

with col2:
    components.html(chart_html, height=600, scrolling=True)
    st.markdown("Results obtained based on [ASTER DEM](https://lpdaac.usgs.gov/products/astgtmv003/), [FEMA data](https://www.fema.gov/data), [Open Street Map](https://www.openstreetmap.org/), and [Landsat Data](https://www.usgs.gov/land-resources/nli/landsat).")
