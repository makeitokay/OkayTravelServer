from flask import jsonify

from okaytravelserver.app import app
from okaytravelserver.db import *


@app.route("/")
def index():
    user = User.query.filter_by(username='admin').first()
    if not user:
        return jsonify({"error": True, "message": "User not found"})
    return jsonify(
        {"error": False,
        "user": {
            "username": user.username,
            "email": user.email
            }
        }
    )

