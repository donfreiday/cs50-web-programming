# Sessions use cookies to ID users

from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# notes = []
# Global to all users, use session["notes"] = [] instead

@app.route("/", methods=["GET", "POST"])
def index():
    # Avoid overwriting the session's "notes" key every page load
    if session.get("notes") is None:
        session["notes"] = []

    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    
    return render_template("index.html", notes=session["notes"])