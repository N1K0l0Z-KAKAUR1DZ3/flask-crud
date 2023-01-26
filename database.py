from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from configuration import app


# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


# address Class/Model
class Address(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  city = db.Column(db.String(100))
  country = db.Column(db.String(100))
  postal_code = db.Column(db.String(100))
  street = db.Column(db.String(100))


  def __init__(self, city, country, postal_code, street):
    self.city = city
    self.country = country
    self.postal_code = postal_code
    self.street = street


# user class/model
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(70), unique = True)
    password = db.Column(db.String(80))

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


# address/user Schema
class AddressSchema(ma.Schema):
  class Meta:
    fields = ('id', 'city', 'country', 'postal_code', 'street')

class UsersSchema(ma.Schema):
  class Meta:
    fields = ('id', 'first_name', 'last_name', 'email', 'password')


# Init schema
address_schema = AddressSchema()
addresses_schema = AddressSchema(many=True)


