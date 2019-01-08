# Flask is a Python micro-framework for quickly implementing web apps
# Flask applications are typically contained in file app.py

# Installation: 
# yay -Syu python-pip
# sudo pip install Flask

# Usage: flask run

from flask import Flask

# __name__ is this file; this file contains our Flask application
app = Flask(__name__)

# route is the part of the url you type in to determine which page is requested
# / is the default page; the function immediately underneath @app.route is associated with the route
@app.route("/")
def index():
    return "Hello, world!"

@app.route("/don")
def don():
    return "Hello, Don!"

@app.route("/becca")
def maria():
    return("<strong>Hello, Becca!</strong>")

# Template for a set of routes
@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}!"