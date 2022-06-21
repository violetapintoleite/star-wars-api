from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Person(db.Model):
    __tablename__ = 'Person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    def __repr__(person):
        return '<Person %r>' % self.name

    def serialize(person):
        return {
            "id": person.id,
            "name": person.name,
        }


class Planet(db.Model):
    __tablename__ = 'Planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    def __repr__(planet):
        return '<Planet>'

    def serialize(planet):
        return {
            "id": planet.id,
            "name": planet.name,
            "climate": planet.climate,
        }


class Favourites(db.Model):
    __tablename__ = 'Favourites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    person_id = db.Column(
        db.Integer, db.ForeignKey('Person.id'), nullable=True)
    planet_id = db.Column(
        db.Integer, db.ForeignKey('Planet.id'), nullable=True)

    def __repr__(favourites):
        return '<Favourites>'

    def serialize(favourites):
        return {
            "id": favourites.id,
            "user_id": favourites.user_id,
            "person_id": favourites.person_id,
            "planet_id": favourites.planet_id,
        }