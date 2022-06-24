"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Person, Planet, Favourites 
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#@app.route('/user', methods=['GET'])
#def handle_hello():

#    response_body = {
#        "msg": "Hello, this is your GET /user response "
#    }

#    return jsonify(response_body), 200

@app.route('/users', methods=['GET'])
def get_all_users():
    
    users = User.get_all_users()
    serialized_users = []
    for user in users:
        serialized_users.append(user.serialize())

    return(jsonify(serialized_users))

@app.route('/users/<int:id>', methods=['GET'])
def get_users_by_id(id):
    
    user = User.get_users_by_id(id)
    
    return(jsonify(user.serialize()))

@app.route('/person', methods=['GET'])
def get_people_list():
    people = Person.get_people_list()
    serialized_people = []
    for person in people:
        serialized_people.append(person.serialize())

    return jsonify(serialized_people), 200

@app.route('/person/<int:id>', methods=['GET'])
def get_single_person(id):
    person = Person.get_single_person(id)
    return jsonify(person.serialize()), 200

@app.route('/planet', methods=['GET'])
def get_planets_list():
    planets = Planet.get_planets_list()
    serialized_planets = []
    for planet in planets:
        serialized_planets.append(planet.serialize())
    return jsonify(serialized_planets), 200

@app.route('/planet/<int:id>', methods=['GET'])
def get_single_planet(id):
    planet = Planet.get_single_planet(id)
    return jsonify(planet.serialize()), 200

   

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
