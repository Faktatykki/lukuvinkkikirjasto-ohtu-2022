from os import getenv
from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Has to defined, but will be overwritten by the Heroku config variables.

class DingDong:
    def __init__(self):
        self.diipadaapa = "10"

    def __str__(self):
        return self.diipadaapa

thing = DingDong()

@app.route("/")
def index():
    return str(thing)

# app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# #important that this import is after variable declaration
# import ui.controller


# @app.route("/")
# def index():
#     '''Ohjaa pääsivulle'''
#     return redirect("/mainpage")
