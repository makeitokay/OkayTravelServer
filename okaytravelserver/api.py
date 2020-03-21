from flask import request, send_file

from okaytravelserver.app import app
from okaytravelserver.city_images import get_city_id
from okaytravelserver.db import *
from okaytravelserver.validate import *
from okaytravelserver.json_templates import *

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

    user = User.query.filter_by(username=data["user"]["user"]["username"]).first()
    if user is None:
        logging.info(f"SYNC WITH REQUEST: {data}\nRETURN UNDEFINED USER ERROR")
        return error("Undefined user")
    if user.access_token != data["accessToken"]:
        logging.info(f"SYNC WITH REQUEST: {data}\nRETURN INVALID ACCESS TOKEN ERROR, USER {user.username}")
        return error("Invalid access token")

    commits = int(data["user"]["user"]["commits"])
    logging.info(f"SYNC FROM USER: {user.username} COMMITS: {commits}")
    if commits > user.commits:
        logging.info(f"UPDATE SERVER DATABASE, USER {user.username}")
        user.update_with_request(data)
        return ok()
    elif commits < user.commits:
        logging.info(f"UPDATE LOCAL DATABASE, USER {user.username}")
        return serialize_user(user)
    return ok("All data is up-to-date")

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


@app.route("/image", methods=["GET"])
def get_image():
    city = request.args.get("city")
    print()
    if city is None:
        return error("Bad request")

    city_id = get_city_id(city)
    if city_id is None:
        return error("City not found")

    return send_file(f"assets/cities/{city_id}.jpg", mimetype="image/jpeg")


@app.route("/download")
def download_app():
    return send_file("assets/OkayTravel.apk", mimetype="application/vnd.android.package-archive")