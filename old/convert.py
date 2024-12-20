""" converts a altr schedule to be compatiblw with the standard efficiency report"""

import pandas as pd
import googlemaps

def convert_csv(input_file, output_file, api_key):
    # Define the mapping for asset names
    asset_name_mapping = {
        'SC101_A': 'v101',
        'SC103_A': 'v102',
        'SC104': 'v104',
        'SC105': 'v105',
        'SC106': 'v106',
        'SC107': 'v107',
        'SC108': 'v108',
        'SC109': 'v109',
        'SC201': 'v201',
        'SC202' : 'v202',
    }

    # Initialize Google Maps client
    gmaps = googlemaps.Client(key=api_key)

    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Change the column name 'mileage' to 'distance'
    df.rename(columns={'mileage': 'distance'}, inplace=True)

    # Map the asset names to match the metrics code
    df['asset'] = df['asset'].map(asset_name_mapping).fillna(df['asset'])

    # Get the distance for each row using Google Maps API
    df['distance'] = df.apply(lambda row: get_google_distance(gmaps, row['pickup_address'], row['dropoff_address']), axis=1)

    # Save the modified DataFrame to a new CSV file
    df.to_csv(output_file, index=False)


def get_google_distance(gmaps, pickup_address, dropoff_address):
    """
    Get the distance between pickup and dropoff addresses using Google Maps API.
    Returns the distance in kilometers rounded to 2 decimal places.
    """
    try:
        # Get the distance matrix response
        result = gmaps.distance_matrix(pickup_address, dropoff_address, mode="driving")
        
        # Extract the distance from the result
        distance = result['rows'][0]['elements'][0]['distance']['value'] / 1000  # Convert from meters to kilometers
        return round(distance, 2)
    
    except Exception as e:
        print(f"Error retrieving distance for {pickup_address} to {dropoff_address}: {e}")
        return None  # In case of error, return None


# Example usage
input_file = r'C:\Users\cyberwitch\Documents\portfolio\ALTR_PROJECT\agent_schedule_2024_10_31.csv'  # Path to your input CSV file
output_file = 'converted_file.csv'  # Path where you want the modified file saved
api_key = 'AIzaSyAYtE2r26Tlw_4tl_BHkpGzj3Kt2Jy5oBo'  # Replace with your Google API key

convert_csv(input_file, output_file, api_key)
