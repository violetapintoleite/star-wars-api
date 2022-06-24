from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    #def __repr__(self):
    #    return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
    @classmethod
    def get_all_users(cls):
        users = cls.query.all()
        return users

    @classmethod
    def get_users_by_id(cls, id):
        users_by_id = cls.query.filter_by(id = id).one_or_none()
        return users_by_id


class Person(db.Model):
    __tablename__ = 'Person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    #def __repr__(person):
    #    return '<Person %r>' % self.name

    def serialize(person):
        return {
            "id": person.id,
            "name": person.name,
        }

    @classmethod
    def get_people_list(cls):
        people = cls.query.all()
        return people

    @classmethod
    def get_single_person(cls, id):
        single_person = cls.query.filter_by(id = id).one_or_none()
        return single_person


class Planet(db.Model):
    __tablename__ = 'Planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    #def __repr__(planet):
    #    return '<Planet>'

    def serialize(planet):
        return {
            "id": planet.id,
            "name": planet.name,
        }

    @classmethod
    def get_planets_list(cls):
        planets = cls.query.all()
        return planets

    @classmethod
    def get_single_planet(cls, id):
        single_planet = cls.query.filter_by(id = id).one_or_none()
        return single_planet


class Favourites(db.Model):
    __tablename__ = 'Favourites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    users = db.relationship(User)
    person_id = db.Column(db.Integer, db.ForeignKey('Person.id'), nullable=True)
    person = db.relationship(Person)
    planet_id = db.Column(db.Integer, db.ForeignKey('Planet.id'), nullable=True)
    planet = db.relationship(Planet)

    def __repr__(favourites):
        return '<Favourites>'

    def serialize(favourites):
        return {
            "id": favourites.id,
            "user_id": favourites.user_id,
            "person_id": favourites.person_id,
            "planet_id": favourites.planet_id,
        }

    @classmethod
    def get_favourites_list(cls):
        favourites = cls.query.all()
        return favourites
    
    @classmethod
    def get_users_favourites(cls, user_id):
        user_favourite = cls.query.filter_by(user_id = user_id).one_or_none()
        return user_favourite

   

   