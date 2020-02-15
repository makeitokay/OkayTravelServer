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
        logging.info(f"RETURN BAD REQUEST ERROR")
        return error("Bad request")

    username = data["username"]
    if User.is_exist(username):
        logging.info(f"RETURN ALREADY EXIST ERROR (USERNAME)")
        return error("Пользователь с таким именем уже существует")
    email = data["email"]
    if User.is_exist_email(email):
        logging.info(f"RETURN ALREADY EXIST ERROR (EMAIL)")
        return error("Пользователь с такой почтой уже существует")

    password_hash = data["passwordHash"]
    avatar = data.get("avatar", None)

    try:
        user = User.create_user(username, email, password_hash, avatar)
        logging.info(f"RETURN SIGN UP RESPONSE, USER {user.username}")
        return sign_up_response(user.username, user.access_token)
    except Exception as e:
        logging.info(f"RETURN UNKNOWN SIGN UP ERROR")
        return error(e)


@app.route("/sync", methods=["POST"])
def sync():
    data = request.json
    logging.info(f"SYNC WITH REQUEST: {data}")

    user = User.query.filter_by(username=data["user"]["user"]["username"]).first()
    if user is None:
        logging.info(f"RETURN UNDEFINED USER ERROR")
        return error("Undefined user")
    if user.access_token != data["accessToken"]:
        logging.info(f"RETURN INVALID ACCESS TOKEN ERROR, USER {user.username}")
        return error("Invalid access token")

    commits = int(data["user"]["user"]["commits"])
    if commits > user.commits:
        logging.info(f"UPDATE SERVER DATABASE, USER {user.username}")
        user.update_with_request(data)
        return ok()
    logging.info(f"UPDATE LOCAL DATABASE, USER {user.username}")
    return serialize_user(user)


@app.route("/auth", methods=["POST"])
def auth():
    data = request.json
    logging.info(f"AUTH WITH REQUEST: {data}")

    if not validate_auth_data(data):
        logging.info("RETURN BAD REQUEST ERROR")
        return error("Bad request")

    user_by_name = User.query.filter_by(username=data["login"]).first()
    user_by_email = User.query.filter_by(email=data["login"]).first()
    if not (user_by_name or user_by_email):
        logging.info(f"RETURN USER NOT FOUND ERROR")
        return error("Такого пользователя не существует")
    user = user_by_name if user_by_name else user_by_email

    if user.password_hash.lower() != data["passwordHash"].lower():
        logging.info(f"RETURN WRONG PASSWORD ERROR, USER {user.username}")
        return error("Неверный пароль")

    logging.info(f"RETURN SERIALIZE USER {user.username}")
    return serialize_user_info(user)