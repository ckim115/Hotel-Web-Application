import googlemaps
import pandas as pd
import geocoder
import json

# Use Google Maps API to locate hotels and save their information
# Read API key from txt
print("Running locator...")
API = open("Google_Maps_API_Key.txt", "r")
APIKey = API.read()
maps = googlemaps.Client(key = APIKey)

def get_current_location():
    g = geocoder.ip('me') # Finds current location
    # Gets the lat and long
    g = g.latlng
    if g is None:
        raise Exception("Coordinates cannot be found")
    return g

def miles_to_meters(miles:float):
    return miles*1_609.344

# Finds current location using lat and long
lat, lon = get_current_location()
loc = (lat,lon)
max_distance = miles_to_meters(15)

# Google Places API request using parameters location, keyword, and max distance
response = maps.places_nearby(
    location=loc,
    keyword='hotel',
    radius=max_distance,
)

hotel_list = response.get('results') # Where we will store all our found hotels
# print(hotel_list)


df = pd.DataFrame(hotel_list)
# Put information of hotels into csv
df.to_csv('list_of_nearby_hotels.csv', index=False)
print("Finished getting list of hotels.")