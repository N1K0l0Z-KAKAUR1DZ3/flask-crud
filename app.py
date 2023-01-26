from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required
from database import app, db, Address, User, address_schema, addresses_schema


# Create an address
@app.route('/address', methods=['POST'])
@jwt_required()
def add_address():
  city = request.json['city']
  country = request.json['country']
  postal_code = request.json['postal_code']
  street = request.json['street']

  new_address = Address(city, country, postal_code, street)

  db.session.add(new_address)
  db.session.commit()

  return address_schema.jsonify(new_address)


# Get All Addresses
@app.route('/address', methods=['GET'])
@jwt_required()
def get_addresses():
  all_addresses = Address.query.all()
  result = addresses_schema.dump(all_addresses)
  return jsonify(result)


# Get Single address
@app.route('/address/<id>', methods=['GET'])
@jwt_required()
def get_address(id):
  address = Address.query.get(id)
  return address_schema.jsonify(address)


# Update a Address
@app.route('/address/<id>', methods=['PUT'])
@jwt_required()
def update_address(id):
  address = Address.query.get(id)

  city = request.json['city']
  country = request.json['country']
  postal_code = request.json['postal_code']
  street = request.json['street']

  address.city = city
  address.country = country
  address.postal_code = postal_code
  address.street = street

  db.session.commit()

  return address_schema.jsonify(address)


# Delete address
@app.route('/address/<id>', methods=['DELETE'])
@jwt_required()
def delete_address(id):
  address = Address.query.get(id)
  db.session.delete(address)
  db.session.commit()

  return address_schema.jsonify(address)


# route for logging user in
@app.route('/login', methods =['POST'])
def login():


    # creates dictionary of form data
    if not request.json['email'] or not request.json['password']:
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )
  
    user = User.query\
        .filter_by(email = request.json['email'])\
        .first()
  
    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )
  
    if check_password_hash(user.password, request.json['password']):
        # generates the JWT Token
        token = create_access_token(identity=user.id)
        return make_response(jsonify({'token' : token}), 201)
    # returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
    )


# signup route
@app.route('/signup', methods =['POST'])
def signup():

    # gets name, email and password
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    password = request.json['password']
  
    # checking for existing user
    user = User.query\
        .filter_by(email = email)\
        .first()
    if not user:
        # database ORM object
        user = User(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = generate_password_hash(password)
        )
        # insert user
        db.session.add(user)
        db.session.commit()
  
        return make_response('Successfully registered.', 201)
    else:
        # returns 202 if user already exists
        return make_response('User already exists. Please Log in.', 202)
  
    
# Run Server
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)