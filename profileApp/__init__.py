from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ProfileApp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dataBase = SQLAlchemy(app)

with app.app_context():
    # Now you're within the application context
    dataBase.create_all()

from profileApp import routes