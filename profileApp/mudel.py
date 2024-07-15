from profileApp import app
from profileApp import dataBase

class User(dataBase.Model):
    id = dataBase.Column(dataBase.Integer(), primary_key=True)
    name = dataBase.Column(dataBase.String(length=30), nullable=False)
    email = dataBase.Column(dataBase.String(length=50), nullable=False, unique=True)
    password = dataBase.Column(dataBase.String(length=50), nullable=False)
    organization = dataBase.Column(dataBase.String(length=40))
    address = dataBase.Column(dataBase.String(length=70))
    city = dataBase.Column(dataBase.String(length=20))
    state = dataBase.Column(dataBase.String(length=20))
    country = dataBase.Column(dataBase.String(length=20))
    postalcode = dataBase.Column(dataBase.String(length=20))

    def __init__(self, name, email, password, organization, address, city, state, country, postalcode):
        super(User, self).__init__()
        self.name = name
        self.email = email
        self.password = password
        self.organization = organization
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.postalcode = postalcode