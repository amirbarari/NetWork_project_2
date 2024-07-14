from profileApp import app
from flask import render_template

@app.route("/")

@app.route("/logrig/")
def log_rig():
    return render_template("LogRig.html")

@app.route("/profile/<user_name>")
def user_profile(user_name):
    return f"user with username : {user_name} loged in"

@app.route("/Admin")
def Admin_page():
    return "welcome admin :)"