from flask import Flask, render_template, request # import flask class methods
from Users import * # import User class
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
                tempHotel = "hotel"+str(i)
                tempHotel = Hotels(lines[5], lines[15], "Great hotel", 408+i, "www."+lines[5]+".com", lines[10])
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

# start of regular functions

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)