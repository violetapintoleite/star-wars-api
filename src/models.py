from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Person(db.Model):
    __tablename__ = 'Person'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    name = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    height = db.Column(db.Integer)

    def __repr__(person):
        return '<Person>' 

    def serialize(person):
        return {
            "id": person.id,
            "uid": person.uid,
            "name": person.name,
            "gender": person.gender,
            "eye_color": person.eye_color,
            "hair_color": person.hair_color,
            "height": person.height
        }

class Planet(db.Model):
    __tablename__ = 'Planet'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    name = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250))
    population = db.Column(db.Integer)
    terrain = db.Column(db.String(250))

    def __repr__(planet):
        return '<Planet>' 

    def serialize(planet):
        return {
            "id": planet.id,
            "uid": planet.uid,
            "name": planet.name,
            "climate": planet.climate,
            "population": planet.population,
            "terrain": planet.terrain,
        }

class Favourites(db.Model):
    __tablename__ = 'Favourites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('User.id'))
    person_id = db.Column(db.Integer, ForeignKey('Person.id'), nullable=True)
    planet_id = db.Column(db.Integer, ForeignKey('Planet.id'), nullable=True)

    def __repr__(favourites):
        return '<Favourites>' 

    def serialize(favourites):
        return {
            "id": favourites.id,
            "user_id": favourites.user_id,
            "person_id": favourites.person_id,
            "planet_id": favourites.planet_id,
        }

