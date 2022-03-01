from os import getenv
from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy

snapp = Flask(__name__)

@snapp.route('/')
def hello_world():
   return "Hello World"

# app = Flask(__name__)
# # Has to defined, but will be overwritten by the Heroku config variables.
# app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = DBManager()

# #important that this import is after variable declaration
# #this is due to the fact that the global variables in the file are set at import,
# #which in turn are dependent on said variable declarations
# #PROBLEM GOES AWAY when we start using classes instead of global scope
# import ui.controller


# @app.route("/")
# def index():
#     '''Ohjaa pääsivulle'''
#     return redirect("/mainpage")
