from flask import Flask, render_template, request, session, redirect, url_for # import flask class methods
from Users import * # import User class
from hotel_additional_info import * # import hotel_additional_info class
from Hotels import * # import Hotel class
import sqlite3

#conn = sqlite3.connect('hotel.db')
#c = conn.cursor()


app = Flask(__name__)


'''
REGULAR FUNCITONS BELOW
'''
# put regular functions definitions before routing functions
def readCSV():
    hotelList = list()
    with open('list_of_nearby_hotels.csv', mode='r') as file:
        csvFile = csv.reader(file)
        i = 0
        for lines in csvFile:
            if lines[5] == 'name': # ignore csv file format / basically checking if name of hotel is name
                continue
            else:
                id = findLocationID(lines[5]) # find the hotel tripadvisor id
                addInfo = findAdditionalInfo(id) # find the hotel price[0] and url[1]
                # reviews = findRatings(id) # find list of 5 reviews *CURRENTLY UNUSED!
                tempHotel = Hotels(lines[5], lines[15], 'Great hotel', addInfo[0], addInfo[1], lines[10])
                hotelList.append(tempHotel)
                i += 1
    #print(hotelList) prints all hotel objects
    for hotel in hotelList:
        hotel.printHotelInfo()
        print() # spacer in between hotel prints
    return hotelList


'''
TEMPLATE FUNCTIONS BELOW
'''
# Login/Initial page
@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    errorMsg = ''
    if request.method == 'POST' and 'emailLogin' in request.form and 'pwLogin' in request.form:
        user = request.form['emailLogin']
        password = request.form['pwLogin']
        if user == '' or password == '': # if user or pw fields are empty, redirect back to login
            return render_template('login.html', errorMsg = 'Failed login: Please fill in all fields for login')
        # check db: if username is in db and if pw is valid for account

        return render_template('index.html', user=user)
    elif request.method == 'POST' and 'emailSignup' in request.form and 'pwSignup' in request.form and 'confPW' in request.form:
        user = request.form['emailSignup']
        password = request.form['pwSignup']
        confPW = request.form['confPW']
        if user == '' or password == '' or confPW == '': # if user or pw or confpw fields are empty, redirect back to login
            return render_template('login.html', errorMsg = 'Failed signup: Please fill in all fields for signup')
        # check db: if username is available
        
        return render_template('index.html', user=user)
    else:
        return render_template('login.html')

# Index Page
@app.route('/index', methods=['POST', 'GET'])
def index_page():
    return render_template('index.html')

# take in user selected location and send in updated index info with hotels in area
# display hotels in area
# call read csv func to get updated csv file with hotels in area
# readCSV()
# send data to page
# def updated_index_page():
# hotel details page/Once button on index is pressed
@app.route('/hotel_details', methods=['POST', 'GET'])
def hotel_info_page():
    hotelList = readCSV()
    return render_template('hotel_details.html', hotels=hotelList, len = len(hotelList))

@app.route('/specific_hotel_details', methods=['POST', 'GET'])
def specific_info_page():
    hotelList = readCSV()
    return render_template('specific_hotel_details.html', specificHotel=hotelList)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)