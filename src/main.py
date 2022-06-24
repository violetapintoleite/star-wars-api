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

@app.route('/favourites', methods=['GET'])
def get_favourites_list():
    favourites = Favourites.get_favourites_list()
    serialized_favourites = []
    for favourite in favourites:
        serialized_favourites.append(favourite.serialize())
    return jsonify(serialized_favourites), 200

@app.route('/users/favourites/<int:user_id>', methods=['GET'])
def get_users_favourites(user_id):
    favourites = Favourites.get_users_favourites(user_id)
    return jsonify(favourites.serialize()), 200

@app.route('/favourites/planet/<int:planet_id>', methods=['POST'])
def add_planet_to_favourites(planet_id):
    favourites = Favourites.get_favourites_list()
    serialized_favourites = []
    for favourite in favourites:
        serialized_favourites.append(favourite.serialize())
    planet_to_add = Planet.get_single_planet(planet_id)
    serialized_favourites.append(planet_to_add.serialize())
    return jsonify(serialized_favourites), 200

@app.route('/favourites/planet/<int:planet_id>', methods=['DELETE'])
def remove_planet(planet_id):
    favourites = Favourites.get_favourites_list()
    serialized_favourites = []
    for favourite in favourites:
        serialized_favourites.append(favourite.serialize())
    
    removed = list(filter(lambda i: i["planet_id"] != planet_id, serialized_favourites))
        
    return jsonify(removed), 200

@app.route('/favourites/person/<int:person_id>', methods=['POST'])
def add_person_to_favourites(person_id):
    favourites = Favourites.get_favourites_list()
    serialized_favourites = []
    for favourite in favourites:
        serialized_favourites.append(favourite.serialize())
    person_to_add = Person.get_single_person(person_id)
    serialized_favourites.append(person_to_add.serialize())
    return jsonify(serialized_favourites), 200

@app.route('/favourites/person/<int:person_id>', methods=['DELETE'])
def remove_person(person_id):
    favourites = Favourites.get_favourites_list()
    serialized_favourites = []
    for favourite in favourites:
        serialized_favourites.append(favourite.serialize())
    
    removed = list(filter(lambda i: i["person_id"] != person_id, serialized_favourites))
        
    return jsonify(removed), 200
   

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
