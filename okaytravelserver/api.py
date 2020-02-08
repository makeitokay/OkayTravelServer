from flask import request

from okaytravelserver.app import app
from okaytravelserver.db import *
from okaytravelserver.validate import *
from okaytravelserver.json_templates import *


@app.route("/create", methods=['POST'])
def create_user():
    data = request.json

    validate = validate_create_user_data(data)
    if not validate:
        return error()

    username = data["username"]
    email = data["email"]
    password_hash = data["password_hash"]
    avatar = data.get("avatar", None)

    try:
        User.create_user(username, email, password_hash, avatar)
        return ok("User was successfully created")
    except Exception as e:
        return error(e)
