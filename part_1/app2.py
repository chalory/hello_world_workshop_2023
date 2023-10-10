from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p style="color: purple>Hello, World!</p>"s