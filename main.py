from flask import Flask
#import Users.py as User

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world!</p>"
