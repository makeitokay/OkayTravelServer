from flask import jsonify


def error(message="unknown error"):
    return jsonify({"error": True, "message": message})


def ok(message="ok"):
    return jsonify({"error": False, "message": message})


def auth_response(username, access_token):
    return jsonify({"error": False, "username": username, "accessToken": access_token})


def serialize_user(user):
    serialized = {
        "user": {
            "username": user.username,
            "email": user.email,
            "password_hash": user.password_hash,
            "avatar": user.avatar
        },
        "trips": []
    }
    for trip in user.trips:
        trip_template = {
            "trip": {
                "own_place": trip.own_place,
                "start_date": trip.start_date.timestamp() * 1000,
                "duration": trip.duration
            },
            "budget": [],
            "places": []
        }
        for budget_el in trip.budget:
            budget_template = {
                "amount": budget_el.amount,
                "category": budget_el.category
            }
            trip_template["budget"].append(budget_template)
        for place in trip.places:
            place_template = {
                "name": place.name,
                "date": place.date.timestamp() * 1000
            }
            trip_template["places"].append(place_template)
        serialized["trips"].append(trip_template)
    return jsonify(serialized)
