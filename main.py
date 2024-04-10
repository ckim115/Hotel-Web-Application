from flask import Flask, render_template, request # import flask class methods
from Users import Users # import User class
from Hotels import Hotels # import Hotel class

app = Flask(__name__)

# put regular functions definitions before routing functions

# functions used to direct webpages
@app.route('/')
@app.route('/login')
def hello_world():
    return render_template('login.html')

@app.route('/index', methods=['POST', 'GET'])
def index_page():
    return render_template('index.html', form=request.form)

@app.route('/HotelInfo', methods=['POST', 'GET'])
def hotel_info_page():
    return render_template('hotel_details.html', form=request.form)

# start of regular functions

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)