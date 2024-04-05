import googlemaps
# atm very basic, just asks for an input for starting location and end location
# Read API key from txt
API = open("Google_Maps_API_Key.txt", "r")
APIKey = API.read()

maps = googlemaps.Client(key = APIKey)

#finding cur location and end location
start = input("Where are you currently?\n")
end = input("Where will you end?\n")

#calculating distance
distance = maps.directions(start, end) #gives instructions to reach destination
#to only get distance and time:
print(distance[0]['legs'][0]['distance']['text'], "and", distance[0]['legs'][0]['duration']['text'])