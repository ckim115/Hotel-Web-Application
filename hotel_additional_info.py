import json

from tripadvisorapi.api import TripadvisorApi
from Ratings import *

API = open("Tripadvisor_API_Key.txt", "r")
APIKey = API.read()
tripadvisor = TripadvisorApi(APIKey)

#ID needed to perform location research. Param for name is 1 hotel name
def findLocationID(hotelName):
    hInfo = tripadvisor.location_search(hotelName)
    res_json = json.loads(hInfo.text)
    if res_json.get('data')[0] == None:
        return None
    return res_json.get('data')[0].get('location_id')

# Returns a list with two items:
#   1) The average cost of a room ($, $$, $$$, etc)
#   2) The url of the hotel, and if there is none, the tripadvisor url
# If id is None, returns ['unknown', 'unknown']
def findAdditionalInfo(hID):
    if hID != None:
        hDetails = tripadvisor.location_details(hID)
        res_json = json.loads(hDetails.text)
        hURL = res_json.get('website')
        if hURL == None:
            hURL = res_json.get('web_url')
        hPrice = res_json.get('price_level')
        if hPrice == None:
            hPrice = res_json.get('unknown')
        return [hPrice, hURL]
    else:
        return ['unknown', 'unknown']

#returns a list of reviews
# If id is None, returns ['unknown']
def findReviews(hID):
    if hID != None:
        hReviews = tripadvisor.location_reviews(hID)
        res_json = json.loads(hReviews.text)
        reviewList = []
        for review in res_json.get('data'):
            r = Ratings(review.get('title'), review.get('published_date'), review.get('rating'), review.get('text'))
            reviewList.append(r)
        return reviewList
    else:
        return ['unknown']

#used for testing
if __name__ == '__main__':
    id = findLocationID("Hotel Zephyr San Francisco")
    print(findAdditionalInfo(id))
    ratings = findReviews(id)
    for r in ratings:
        r.printRatingInfo()