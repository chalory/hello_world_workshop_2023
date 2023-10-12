from flask import Flask

app = Flask(__name__)




@app.route("/hello")
def hello_world():
    return "<div style='background-color: red'> <h1 style='color:blue;'>Hello, Computer Wizards!!</h1></div>"


# @app.route("/hello_1")
# def hello_world():
#     return "<div style='background-color: black; margin: 0px; height: 100%;'>   <h1 style='color: violet; text-align: center;'>Hello, Computer Wizards!!</h1></div>"


