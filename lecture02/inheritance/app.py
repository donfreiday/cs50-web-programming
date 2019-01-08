from flask import Flask, render_template

app = Flask(__name__)

# default route
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("more.html")