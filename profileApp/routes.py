from profileApp import app
from flask import render_template, request

@app.route("/")
@app.route("/logrig/", methods=['GET', 'POST'])
def log_rig():
    form_name = request.form.get("name")
    if form_name == "sign-in-form":
        user_name = request.form["user-name"]
        password = request.form["password"]
    elif form_name == "sign-up-form":
        name = request.form["name"]
    return render_template("LogRig.html")

@app.route("/profile/<user_name>")
def user_profile(user_name):
    return f"user with username : {user_name} loged in"

@app.route("/Admin")
def Admin_page():
    return "welcome admin :)"