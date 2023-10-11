from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p style='color:blue;'>Hello, World!</p>"



@app.route("/hello")
def hello_world():
    return "<p style='color:blue;'>Hello, Computer Wizards!!</p>"
