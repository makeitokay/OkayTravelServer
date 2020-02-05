from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from okaytravelserver.config import DATABASE_URI, TRACK_MODIFICATIONS, JSON_AS_ASCII


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = TRACK_MODIFICATIONS
app.config["JSON_AS_ASCII"] = JSON_AS_ASCII

db = SQLAlchemy(app)