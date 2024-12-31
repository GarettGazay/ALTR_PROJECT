import pandas as pd
import googlemaps
import folium
from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster
from decouple import config
import random

# Function to geocode the address
def geocode_address(address, gmaps=None):
    if gmaps:
        geocode_result = gmaps.geocode(address)
        if geocode_result:
            lat = geocode_result[0]['geometry']['location']['lat']
            lng = geocode_result[0]['geometry']['location']['lng']
            return lat, lng
    geolocator = Nominatim(user_agent="route_plotter")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    return None, None

# Function to plot addresses on the map and draw the routes
def plot_routes_on_map(csv_file, output_image='output_map.html', google_api_key=config('GMAPS_PAID')):
    # Initialize Google Maps client
    gmaps = googlemaps.Client(key=google_api_key)

    # Load the CSV with addresses and assets
    df = pd.read_csv(csv_file)
    
    # Create a base map centered on an arbitrary location (e.g., USA)
    base_map = folium.Map(location=[37.7749, -122.4194], zoom_start=10, tiles='cartodb dark_matter')
    
    # Use the Google Maps URL for the tiles, passing your API key into the URL
    # google_map = folium.TileLayer(
    #     tiles=f'https://mt0.googleusercontent.com/vt/lyrs=m&x={{x}}&y={{y}}&z={{z}}&scale=2&key={google_api_key}',
    #     attr='Google Maps',
    #     name='Google Maps'
    # ).add_to(base_map)
    
    # Create a dictionary for assets and their corresponding colors
    asset_colors = {}
    color_palette = ['#FF5733', '#33FF57', '#3357FF', '#F33FFF', '#FF3333', '#33F3FF', '#F3F333']

    # Create a marker cluster
    marker_cluster = MarkerCluster().add_to(base_map)

    # Create FeatureGroups to allow toggling assets on/off
    feature_groups = {}

    # Iterate over each row in the CSV to plot routes
    for index, row in df.iterrows():
        pickup_address = row['pickup_address']
        dropoff_address = row['dropoff_address']
        asset = row['asset']
        
        # Get coordinates for pickup and dropoff addresses
        pickup_lat, pickup_lon = geocode_address(pickup_address, gmaps)
        dropoff_lat, dropoff_lon = geocode_address(dropoff_address, gmaps)
        
        if pickup_lat and pickup_lon and dropoff_lat and dropoff_lon:
            # If asset color is not assigned, assign a random color
            if asset not in asset_colors:
                asset_colors[asset] = random.choice(color_palette)

            # Create a FeatureGroup for the asset if not already created
            if asset not in feature_groups:
                feature_groups[asset] = folium.FeatureGroup(name=asset).add_to(base_map)

            # Plot the pickup and dropoff points
            folium.Marker(
                location=[pickup_lat, pickup_lon],
                popup=f"{asset} Pickup: {pickup_address}",
                icon=folium.Icon(color=asset_colors[asset])
            ).add_to(feature_groups[asset])
            
            folium.Marker(
                location=[dropoff_lat, dropoff_lon],
                popup=f"{asset} Dropoff: {dropoff_address}",
                icon=folium.Icon(color=asset_colors[asset])
            ).add_to(feature_groups[asset])
            
            # Plot the route (line) between pickup and dropoff
            folium.PolyLine(
                locations=[(pickup_lat, pickup_lon), (dropoff_lat, dropoff_lon)],
                color=asset_colors[asset],
                weight=3,
                opacity=0.7
            ).add_to(feature_groups[asset])

    # Add a legend to the map
    legend_html = f'<div style="position: fixed; bottom: 10px; left: 10px; background-color: white; padding: 10px; border-radius: 5px;">'
    legend_html += '<b>Asset Legend:</b><br>'
    for asset, color in asset_colors.items():
        legend_html += f'<span style="color:{color};">{asset}</span><br>'
    legend_html += '</div>'

    # Add the legend to the map as an HTML element
    base_map.get_root().html.add_child(folium.Element(legend_html))

    # Add LayerControl to allow toggling assets
    folium.LayerControl().add_to(base_map)

    # Save the map to an HTML file
    base_map.save(output_image)
    print(f"Map saved to {output_image}")

# Example usage:
csv_file = r'C:\Users\cyberwitch\Documents\portfolio\ALTR_PROJECT\data\2024-06-06.csv'  # Replace with the path to your CSV file
google_api_key = config('GMAPS_PAID')  # Replace with your Google API key
plot_routes_on_map(csv_file, google_api_key=google_api_key)
