from flask import jsonify


def error(message="unknown error"):
    return jsonify({"error": True, "message": message})


def ok(message="ok"):
    return jsonify({"error": False, "message": message})