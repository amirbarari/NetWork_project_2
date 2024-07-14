from profileApp import app
from flask import render_template

@app.route("/")

@app.route("/logrig/")
def log_rig():
    return render_template("LogRig.html")
