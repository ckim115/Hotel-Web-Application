from flask import Flask, render_template, request # import flask class methods
from Users import * # import User class
from hotel_additional_info import * # import hotel_additional_info class
from Hotels import * # import Hotel class

app = Flask(__name__)

# put regular functions definitions before routing functions
def readCSV():
    hotelList = list()
    with open('list_of_nearby_hotels.csv', mode='r') as file:
        csvFile = csv.reader(file)
        i = 0
        for lines in csvFile:
            if lines[5] == "name": # ignore csv file format / basically checking if name of hotel is name
                continue
            else:
                id = findLocationID(lines[5]) # find the hotel tripadvisor id
                addInfo = findAdditionalInfo(id) # find the hotel price[0] and url[1]
                # reviews = findRatings(id) # find list of 5 reviews *CURRENTLY UNUSED!
                tempHotel = Hotels(lines[5], lines[15], "Great hotel", addInfo[0], addInfo[1], lines[10])
                hotelList.append(tempHotel)
                i += 1
    #print(hotelList) prints all hotel objects
    for hotel in hotelList:
        hotel.printHotelInfo()
        print() # spacer in between hotel prints
    return hotelList

# functions used to direct webpages
@app.route('/')
@app.route('/login')
def hello_world():
    return render_template('login.html')

@app.route('/index', methods=['POST', 'GET'])
def index_page():
    return render_template('index.html', form=request.form)

# take in user selected location and send in updated index info with hotels in area
# display hotels in area
# call read csv func to get updated csv file with hotels in area
# readCSV()
# send data to page
# def updated_index_page():

@app.route('/hotel_details', methods=['POST', 'GET'])
def hotel_info_page():
    hotelList = readCSV()
    return render_template('hotel_details.html', hotels=hotelList, len = len(hotelList), form=request.form)

@app.route('/specific_hotel_details', methods=['POST', 'GET'])
def specific_info_page():
    hotelList = readCSV()
    return render_template('specific_hotel_details.html', specificHotel=hotelList)

# start of regular functions

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)