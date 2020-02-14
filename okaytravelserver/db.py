from uuid import uuid4

from okaytravelserver.app import db
from okaytravelserver.utils import get_current_datetime, parse_date_string

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    avatar = db.Column(db.String(50), nullable=True)

    access_token = db.Column(db.String(36), nullable=False, default=lambda: str(uuid4()))
    last_update_datetime = db.Column(db.DateTime, nullable=True, default=get_current_datetime())

    trips = db.relationship("Trip", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

    def update_with_request(self, request):
        user = request["user"]
        trips = user["trips"]
        user_info = user["user"]

        self.username = user_info["username"]
        self.email = user_info["email"]
        self.password_hash = user_info["passwordHash"]
        self.avatar = user_info["avatar"]
        self.last_update_datetime = get_current_datetime()

        for trip_info in trips:
            trip_remote_id = int(trip_info["trip"]["remoteId"])
            own_place = trip_info["trip"]["ownPlace"]
            start_date = parse_date_string(trip_info["trip"]["startDate"])
            duration = int(trip_info["trip"]["duration"])
            trip = Trip.query.filter_by(remote_id=trip_remote_id, user_id=self.id).first()
            if trip is None:
                trip = Trip.create_trip(trip_remote_id, self.id, own_place, start_date, duration)
            else:
                trip.own_place = own_place
                trip.start_date = start_date
                trip.duration = duration

            for budget_element_info in trip_info["budget"]:
                budget_remote_id = int(budget_element_info["remoteId"])
                amount = int(budget_element_info["amount"])
                category = budget_element_info["category"]

                budget_element = BudgetElement.query.filter_by(remote_id=budget_remote_id, trip_id=trip.id).first()
                if budget_element is None:
                    BudgetElement.create_budget_element(budget_remote_id, trip.id, amount, category)
                else:
                    budget_element.amount = amount
                    budget_element.category = category

            for place_info in trip_info["places"]:
                place_remote_id = int(place_info["remoteId"])
                name = place_info["name"]
                date = parse_date_string(place_info["date"])

                place = Place.query.filter_by(remote_id=place_remote_id, trip_id=trip.id).first()
                if place is None:
                    Place.create_place(place_remote_id, trip.id, name, date)
                else:
                    place.name = name
                    place.date = date

        db.session.commit()



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

    @staticmethod
    def create_trip(remote_id, user_id, own_place, start_date, duration):
        trip = Trip(remote_id=remote_id, user_id=user_id, own_place=own_place, start_date=start_date, duration=duration)
        db.session.add(trip)
        db.session.commit()
        return trip


class BudgetElement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    remote_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(30), nullable=False)
    trip_id = db.Column(db.Integer, db.ForeignKey("trip.id"), nullable=False)

    @staticmethod
    def create_budget_element(remote_id, trip_id, amount, category):
        budget_element = BudgetElement(remote_id=remote_id, trip_id=trip_id, amount=amount, category=category)
        db.session.add(budget_element)
        db.session.commit()
        return budget_element


class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    remote_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    trip_id = db.Column(db.Integer, db.ForeignKey("trip.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)

    @staticmethod
    def create_place(remote_id, trip_id, name, date):
        place = Place(remote_id=remote_id, trip_id=trip_id, name=name, date=date)
        db.session.add(place)
        db.session.commit()
        return place


db.create_all()
