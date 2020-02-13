from flask import request
import datetime as dt

from okaytravelserver.app import app
from okaytravelserver.db import *
from okaytravelserver.validate import *
from okaytravelserver.json_templates import *
from okaytravelserver.config import DATE_FORMAT, DATETIME_FORMAT

import logging

logging.basicConfig(level=logging.DEBUG)

@app.route("/create", methods=['POST'])
def create_user():
    data = request.json
    logging.info(f"CREATE USER WITH REQUEST: {data}")

    if not validate_create_user_data(data):
        return error("Bad request")

    username = data["username"]
    if User.is_exist(username):
        return error("Пользователь с таким именем уже существует")
    email = data["email"]
    if User.is_exist_email(email):
        return error("Пользователь с такой почтой уже существует")

    password_hash = data["passwordHash"]
    avatar = data.get("avatar", None)

    try:
        user = User.create_user(username, email, password_hash, avatar)
        return sign_up_response(user.username, user.access_token)
    except Exception as e:
        return error(e)


@app.route("/sync", methods=["POST"])
def sync():
    data = request.json
    logging.info(f"SYNC WITH REQUEST: {data}")

    user = User.query.filter_by(username=data["user"]["username"]).first()
    if user is None:
        return error("Undefined user")
    if user.access_token != data["accessToken"]:
        return error("Invalid access token")

    last_update_datetime = data["user"]["lastUpdateDatetime"]
    from_timestamp = dt.datetime.strptime(last_update_datetime, DATETIME_FORMAT)
    if from_timestamp > user.last_update_datetime:
        # TODO: записать изменения в базу данных
        return ok()
    else:
        return serialize_user(user)


@app.route("/auth", methods=["POST"])
def auth():
    data = request.json
    logging.info(f"AUTH WITH REQUEST: {data}")

    if not validate_auth_data(data):
        return error("Bad request")

    user_by_name = User.query.filter_by(username=data["login"]).first()
    user_by_email = User.query.filter_by(email=data["login"]).first()
    if not (user_by_name or user_by_email):
        return error("Такого пользователя не существует")
    user = user_by_name if user_by_name else user_by_email

    if user.password_hash.lower() != data["passwordHash"].lower():
        return error("Неверный пароль")

    return serialize_user_info(user)