import googlemaps
import pandas as pd
import time
# atm very basic, just asks for an input for starting location and end location
# Read API key from txt
API = open("Google_Maps_API_Key.txt", "r")
APIKey = API.read()

maps = googlemaps.Client(key = APIKey)

def miles_to_meters(miles:float):
    return miles*1_609.344

#finding cur location and end location
loc = (37.3507608,-122.0264249) # TODO: figure out how to find current location
max_distance = miles_to_meters(15)

response = maps.places_nearby(
    location=loc,
    keyword='hotel',
    radius=max_distance,
)
print(response.keys())
hotel_list = response.get('results') #where we will store all our found hotels

df = pd.DataFrame(hotel_list)
df.to_csv('list_of_nearby_hotels.csv', index=False)

# #calculating distance
# distance = maps.directions(start, end) #gives instructions to reach destination
# #to only get distance and time:
# print(distance[0]['legs'][0]['distance']['text'], "and", distance[0]['legs'][0]['duration']['text'])