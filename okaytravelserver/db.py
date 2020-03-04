from uuid import uuid4

from okaytravelserver.app import db
from okaytravelserver.utils import parse_date_string


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    avatar = db.Column(db.String(50), nullable=True)

    access_token = db.Column(db.String(36), nullable=False, default=lambda: str(uuid4()))
    commits = db.Column(db.Integer, nullable=False, default=0)

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
        self.avatar = user_info.get("avatar", None)
        self.commits = user_info["commits"]

        for trip_info in trips:
            trip_uuid = trip_info["trip"]["uuid"]
            own_place = trip_info["trip"]["ownPlace"]
            full_address = trip_info["trip"]["fullAddress"]
            start_date = parse_date_string(trip_info["trip"]["startDate"])
            duration = int(trip_info["trip"]["duration"])
            trip = Trip.query.filter_by(uuid=trip_uuid).first()
            if trip is None:
                trip = Trip.create_trip(trip_uuid, self.id, own_place, full_address, start_date, duration)
            else:
                trip.own_place = own_place
                trip.full_address = full_address
                trip.start_date = start_date
                trip.duration = duration

            for budget_element_info in trip_info["budget"]:
                budget_uuid = budget_element_info["uuid"]
                amount = int(budget_element_info["amount"])
                category = budget_element_info["category"]

                budget_element = BudgetElement.query.filter_by(uuid=budget_uuid).first()
                if budget_element is None:
                    BudgetElement.create_budget_element(budget_uuid, trip.id, amount, category)
                else:
                    budget_element.amount = amount
                    budget_element.category = category

            for place_info in trip_info["places"]:
                place_uuid = place_info["uuid"]
                name = place_info.get("name", None)
                full_address = place_info.get("fullAddress", None)
                latitude = place_info["latitude"]
                longitude = place_info["longitude"]
                date = parse_date_string(place_info["date"])

                place = Place.query.filter_by(uuid=place_uuid).first()
                if place is None:
                    Place.create_place(place_uuid, trip.id, name, full_address, latitude, longitude, date)
                else:
                    place.name = name
                    place.full_address = full_address
                    place.latitude = latitude
                    place.longitude = longitude
                    place.date = date

            for thing_info in trip_info["things"]:
                thing_uuid = thing_info["uuid"]
                thing_name = thing_info["name"]

                thing = Thing.query.filter_by(uuid=thing_uuid).first()
                if thing is None:
                    Thing.create_thing(thing_uuid, trip.id, thing_name)
                else:
                    thing.name = thing_name

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
    uuid = db.Column(db.String(36), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    own_place = db.Column(db.String(50), nullable=False)
    full_address = db.Column(db.String(150), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=True)

    budget = db.relationship("BudgetElement", backref="trip", lazy=True)
    places = db.relationship("Place", backref="trip", lazy=True)

    @staticmethod
    def create_trip(uuid, user_id, own_place, full_address, start_date, duration):
        trip = Trip(uuid=uuid, user_id=user_id, own_place=own_place, full_address=full_address, start_date=start_date,
                    duration=duration)
        db.session.add(trip)
        db.session.commit()
        return trip


class BudgetElement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), nullable=False, unique=True)
    amount = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(30), nullable=False)
    trip_id = db.Column(db.Integer, db.ForeignKey("trip.id"), nullable=False)

    @staticmethod
    def create_budget_element(uuid, trip_id, amount, category):
        budget_element = BudgetElement(uuid=uuid, trip_id=trip_id, amount=amount, category=category)
        db.session.add(budget_element)
        db.session.commit()
        return budget_element


class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=True)
    full_address = db.Column(db.String(150), nullable=True)
    latitude = db.Column(db.String(10), nullable=False)
    longitude = db.Column(db.String(10), nullable=False)
    trip_id = db.Column(db.Integer, db.ForeignKey("trip.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)

    @staticmethod
    def create_place(uuid, trip_id, name, full_address, latitude, longitude, date):
        place = Place(uuid=uuid, trip_id=trip_id, name=name, full_address=full_address, latitude=latitude,
                      longitude=longitude, date=date)
        db.session.add(place)
        db.session.commit()
        return place


class Thing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(36), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    trip_id = db.Column(db.Integer, db.ForeignKey("trip.id"), nullable=False)

    @staticmethod
    def create_thing(uuid, trip_id, name):
        thing = Thing(uuid=uuid, trip_id=trip_id, name=name)
        db.session.add(thing)
        db.session.commit()
        return thing


db.create_all()
