from flask import Flask # import flask class
from Users import * # import User class
#import Users.py as User

app = Flask(__name__)

# functions used to direct webpages

@app.route("/")
@app.route("/index")
def hello_world():
    return "<p>Hello world!</p>"

@app.route("/index")
def hello2():
    pass

# start of regular functions

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)