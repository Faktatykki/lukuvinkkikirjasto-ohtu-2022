from os import getenv
from dotenv import load_dotenv
from flask import Flask, redirect
from ui.controller import Controller

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = getenv("SECRET_KEY")
controller = Controller(app)
load_dotenv(".db_env")

@app.route("/")
def index():
    return controller.browse_tips()

@app.route("/add", methods=["POST"])
def add_tip():
    return controller.add_tip()

@app.route("/signup", methods=["POST"])
def add_new_user():
    return controller.add_new_user()

@app.route("/signup", methods=["GET"])
def get_signup_page():
    return controller.get_signup_page()

@app.route("/logout")
def logout():
    return controller.logout()

@app.route("/login", methods=["POST"])
def login():
    return controller.login()

@app.route("/login", methods=["GET"])
def login_page():
    return controller.login_page()