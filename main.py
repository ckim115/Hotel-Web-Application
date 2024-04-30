from flask import Flask, render_template, request, session, redirect, url_for # import flask class methods
from Users import * # import User class
from hotel_additional_info import * # import hotel_additional_info class
from Hotels import * # import Hotel class
import sqlite3

conn = sqlite3.connect('hotel.db', check_same_thread=False)
c = conn.cursor()

app = Flask(__name__)

hotelList = list()

'''
REGULAR FUNCITONS BELOW
'''
# put regular functions definitions before routing functions
def readCSV():
    global hotelList
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
    # for hotel in hotelList:
    #     hotel.printHotelInfo()
    #     print() # spacer in between hotel prints
    return hotelList

hotelList = readCSV()

'''
TEMPLATE FUNCTIONS BELOW
'''
# session key
app.secret_key = b'thisKeyIsSecret123'

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
        # check db: if a user exists with the username and if pw is valid for account
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (user, password,))
        temp = c.fetchall()
        print(temp)
        if temp == []: # if user is not in database, redirect back to login
            return render_template('login.html', errorMsg = 'Failed login: User not in database')
        '''
        Made it to this point, successful login
        create session
        '''
        session['user'] = user
        return render_template('index.html', user=user)
    elif request.method == 'POST' and 'emailSignup' in request.form and 'pwSignup' in request.form and 'confPW' in request.form:
        user = request.form['emailSignup']
        password = request.form['pwSignup']
        confPW = request.form['confPW']
        if user == '' or password == '' or confPW == '': # if user or pw or confpw fields are empty, redirect back to login
            return render_template('login.html', errorMsg = 'Failed signup: Please fill in all fields for signup')
        if password != confPW:
            return render_template('login.html', errorMsg = 'Failed signup: Passwords do not match')
        # check db: if username is available
        c.execute("SELECT * FROM users WHERE username=?", (user,))
        temp = c.fetchall()
        print(temp)
        if not(temp == []):
            return render_template('login.html', errorMsg = 'Failed signin: Please choose another username')
        '''
        Made it to this point, successful signup
        create session
        '''
        c.execute("INSERT INTO users VALUES(?, ?)", (user, password))
        session['user'] = user
        return render_template('index.html', user=user)
    else:
        return render_template('login.html')

# Index Page
@app.route('/index/', methods=['POST', 'GET'])
def index_page():
    user = session['user'] # if session doesnt exist
    if user == None:
        return url_for('/logout')
    return render_template('index.html', user=user)

# take in user selected location and send in updated index info with hotels in area
# display hotels in area
# call read csv func to get updated csv file with hotels in area
# readCSV()
# send data to page
# def updated_index_page():
# hotel details page/Once button on index is pressed
@app.route('/hotel_details', methods=['POST', 'GET'])
def hotel_info_page():
    user = session['user'] # if session doesnt exist
    if user == None:
        return url_for('/logout')
    global hotelList
    return render_template('hotel_details.html', hotels=hotelList, len = len(hotelList))

@app.route('/hotel_details/<hotel>/<address>/<cost>/<rating>/', methods=['POST', 'GET'])
def bookmark(hotel, address, cost, rating):
    user = session['user'] # if session doesnt exist
    if user == None:
        return url_for('/logout')
    print("sent data:", hotel, address, cost, rating)
    global hotelList
    if hotel == 'hotel_details.css' or address == 'hotel_details.css' or cost == 'hotel_details.css' or rating == 'hotel_details.css': # if hotel_details crept into function
        return render_template('hotel_details.html', hotels=hotelList, len = len(hotelList))
    print("current user:", session['user'])
    username = session['user']
    # check db: if hotel is already in db
    c.execute("SELECT * FROM hotels WHERE name=?", (hotel,))
    temp = c.fetchall()
    print(temp)
    if temp == []: # if hotel is not in db, add to db
        c.execute("INSERT INTO hotels VALUES(?, ?, ?, ?, ?)", (username, hotel, address, cost, rating,))
    return render_template('hotel_details.html', hotels=hotelList, len = len(hotelList))

@app.route('/userSavedHotels/', methods=['POST', 'GET'])
def userSavedHotels():
    user = session['user'] # if session doesnt exist
    if user == None:
        return url_for('/logout')
    c.execute("SELECT H.name, H.address, H.cost, H.rating FROM users U, hotels H WHERE U.username = H.username")
    userHotels = c.fetchall()
    print(userHotels)
    return render_template('userSavedHotels.html', hotels = userHotels)

@app.route('/userSavedHotels/<hotel>/', methods=['POST', 'GET'])
def userSavedHotels_Delete(hotel):
    user = session['user'] # if session doesnt exist
    if user == None:
        return url_for('/logout')
    if hotel == "hotel":
        userHotels = c.fetchall()
        print(userHotels)
        return render_template('userSavedHotels.html', hotels = userHotels)
    c.execute("DELETE FROM hotels WHERE name=? AND username=?", (hotel, user,)) # delete hotel
    c.execute("SELECT H.name, H.address, H.cost, H.rating FROM users U, hotels H WHERE U.username = H.username") # query user hotels again
    userHotels = c.fetchall() # fetch hotels
    print(userHotels)
    return render_template('userSavedHotels.html', hotels = userHotels) # reload bookmark page

@app.route('/logout/')
def logout():
    session.pop('user', None) # destroy session variable
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)