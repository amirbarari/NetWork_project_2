from profileApp import app
from flask import render_template

@app.route("/")

@app.route("/log-rig")
def log_rig():
    return render_template("log-rig.html")
