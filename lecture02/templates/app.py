import datetime

# render_template is a function in flask
from flask import Flask, render_template

app = Flask(__name__)

# Default route
@app.route("/")
def newyears():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("index.html", headline="Is it the new year?", new_year=new_year)