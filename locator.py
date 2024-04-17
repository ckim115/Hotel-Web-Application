import googlemaps
import pandas as pd
import geocoder

# Use Google Maps API to locate hotels and save their information

# Read API key from txt
API = open("Google_Maps_API_Key.txt", "r")
APIKey = API.read()

maps = googlemaps.Client(key = APIKey)

def get_current_location():
    g = geocoder.ip('me') #finds cur location
    g = g.latlng
    if g is None:
        raise Exception("Coordinates cannot be found")
    return g

def miles_to_meters(miles:float):
    return miles*1_609.344

#finding cur location and end location
lat, lon = get_current_location()
loc = (lat,lon)
max_distance = miles_to_meters(15)

response = maps.places_nearby(
    location=loc,
    keyword='hotel',
    radius=max_distance,
)

hotel_list = response.get('results') #where we will store all our found hotels

df = pd.DataFrame(hotel_list)
df.to_csv('list_of_nearby_hotels.csv', index=False)