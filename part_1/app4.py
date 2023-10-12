from flask import Flask, render_template

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)


@app.route('/')
def home_page():
  return render_template(
      'base.html',  # Template file path, starting from the templates folder. 
  )
