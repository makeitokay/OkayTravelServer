from flask import jsonify

from okaytravelserver.app import app


@app.route("/")
def index():
    return jsonify({"error": False, "message": "There will be OkayTravelAPI soon"})
