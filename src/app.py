from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from os import getenv



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL") # Has to defined, but will be overwritten by the Heroku config variables.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#important that this import is after variable declaration
import ui.controller


@app.route("/")
def index():
    print('haloo')
    return redirect("/mainpage")
