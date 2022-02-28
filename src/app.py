from os import getenv
from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Has to defined, but will be overwritten by the Heroku config variables.
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)#is this necessary...?

#important that this import is after variable declaration
from ui.controller import Controller

@app.route("/")
def index():
    '''Ohjaa pääsivulle'''
    return redirect("/mainpage")
