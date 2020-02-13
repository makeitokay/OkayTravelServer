from uuid import uuid4

from okaytravelserver.app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    avatar = db.Column(db.String(50), nullable=True)

    access_token = db.Column(db.String(36), nullable=False, default=lambda: str(uuid4()))
    last_update_datetime = db.Column(db.DateTime, nullable=True)

    trips = db.relationship("Trip", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

    @staticmethod
    def create_user(username, email, password_hash, avatar=None):
        user = User(username=username, email=email, password_hash=password_hash, avatar=avatar)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def is_exist(username):
        return User.query.filter_by(username=username).first() is not None

    @staticmethod
    def is_exist_email(email):
        return User.query.filter_by(email=email).first() is not None


class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    remote_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    own_place = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=True)

    budget = db.relationship("BudgetElement", backref="trip", lazy=True)
    places = db.relationship("Place", backref="trip", lazy=True)


class BudgetElement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    remote_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(30), nullable=False)
    trip_id = db.Column(db.Integer, db.ForeignKey("trip.id"), nullable=False)


class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    remote_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    trip_id = db.Column(db.Integer, db.ForeignKey("trip.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)


db.create_all()
