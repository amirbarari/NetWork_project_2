from profileApp import app, dataBase
from flask import render_template, request, redirect, url_for
from profileApp.mudel import User


@app.route("/logrig/", methods=['GET', 'POST'])
def log_rig():
    if request.method == 'POST':
        form_name = request.form.get("form-name")
        if form_name == "sign-in-form":
            user_name = request.form["user-name"]
            password = request.form["password"]
            if user_name == "Admin" and password == password:
                return redirect(url_for("Admin_page"))
            return redirect(url_for("user_profile", user_name=user_name))
        elif form_name == "sign-up-form":
            name = request.form["name"]
            email = request.form["email"]
            address = request.form["address"]
            state = request.form["state"]
            password = request.form["password"]
            city = request.form["city"]
            country = request.form["country"]
            postalcode = request.form["postalcode"]
            organization = request.form["organization"]
            #add to database
            new_user = User(name=name, email=email, password=password, organization=organization, address=address,
                            city=city, state=state, country=country, postalcode=postalcode)
            #dataBase.session.add(new_user)
            #dataBase.session.commit()

            return redirect(url_for("user_profile", user_name=name))
    return render_template("LogRig.html")

@app.route("/profile/<user_name>")
def user_profile(user_name):
    return render_template("profile.html")

@app.route("/Admin")
def Admin_page():
    return "welcome admin :)"