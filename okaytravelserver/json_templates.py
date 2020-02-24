from flask import jsonify

from okaytravelserver.utils import parse_date


def error(message="unknown error"):
    return jsonify({"error": True, "message": message})


def ok(message="ok"):
    return jsonify({"error": False, "message": message})


def sign_up_response(username, access_token):
    return jsonify({"error": False, "username": username, "accessToken": access_token})


def serialize_user(user):
    serialized = {
        "user": {
            "user": {
                "username": user.username,
                "email": user.email,
                "passwordHash": user.password_hash,
                "avatar": user.avatar,
                "accessToken": user.access_token,
                "commits": user.commits
            },
            "trips": []
        }
    }
    for trip in user.trips:
        trip_template = {
            "trip": {
                "uuid": trip.uuid,
                "ownPlace": trip.own_place,
                "fullAddress": trip.full_address,
                "startDate": parse_date(trip.start_date),
                "duration": trip.duration
            },
            "budget": [],
            "places": []
        }
        for budget_el in trip.budget:
            budget_template = {
                "uuid": budget_el.uuid,
                "amount": budget_el.amount,
                "category": budget_el.category
            }
            trip_template["budget"].append(budget_template)
        for place in trip.places:
            place_template = {
                "uuid": place.uuid,
                "name": place.name,
                "fullAddress": place.full_address,
                "date": parse_date(place.date)
            }
            trip_template["places"].append(place_template)
        serialized["user"]["trips"].append(trip_template)
    return jsonify(serialized)


def serialize_user_info(user):
    serialized = {
        "error": False,
        "message": "",
        "user": {
            "username": user.username,
            "email": user.email,
            "passwordHash": user.password_hash,
            "avatar": user.avatar,
            "accessToken": user.access_token
        }
    }
    return jsonify(serialized)
