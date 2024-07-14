from profileApp import app
from flask import render_template

@app.route("/")
def start():
    return "<h1>hello world</h1>"

@app.route("/logrig/")
def log_rig():
    return render_template("LogRig.html")
