from flask import request
import datetime as dt

from okaytravelserver.app import app
from okaytravelserver.db import *
from okaytravelserver.validate import *
from okaytravelserver.json_templates import *
from okaytravelserver.config import DATE_FORMAT, DATETIME_FORMAT


@app.route("/create", methods=['POST'])
def create_user():
    data = request.json

    if not validate_create_user_data(data):
        return error("Bad request")

    username = data["username"]
    email = data["email"]
    password_hash = data["passwordHash"]
    avatar = data.get("avatar", None)

    try:
        user = User.create_user(username, email, password_hash, avatar)
        return ok(user.access_token)
    except Exception as e:
        return error(e)


@app.route("/sync", methods=["POST"])
def sync():
    access_token = request.args.get("accessToken", None)
    data = request.json

    if not validate_sync_data(data):
        return error("Bad request")
    user = User.query.filter_by(username=data["username"]).first()
    if user is None:
        return error("Undefined user")
    if user.access_token != access_token:
        return error("Invalid access token")

    last_update_datetime = data["lastUpdateDatetime"]
    if last_update_datetime is None:
        return serialize_user(user)

    from_timestamp = dt.datetime.fromtimestamp(int(last_update_datetime))
    if from_timestamp > user.last_update_datetime:
        # TODO: записать изменения в базу данных
        pass
    else:
        return serialize_user(user)


@app.route("/auth", methods=["POST"])
def auth():
    data = request.json

    if not validate_auth_data(data):
        return error("Bad request")

    user_by_name = User.query.filter_by(username=data["login"]).first()
    user_by_email = User.query.filter_by(email=data["login"]).first()
    if not (user_by_name or user_by_email):
        return error("User not found")
    user = user_by_name if user_by_name else user_by_email

    if user.password_hash.lower() != data["passwordHash"].lower():
        return error("Wrong password")

    return ok(user.access_token)