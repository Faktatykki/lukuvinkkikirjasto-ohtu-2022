from os import getenv
from dotenv import load_dotenv
from flask import Flask, request
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


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        return controller.add_new_user()
    return controller.get_signup_page()

@app.route("/logout")
def logout():
    return controller.logout()


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        return controller.login()
    return controller.login_page()

@app.route("/search", methods=["POST", "GET"])
def search_page():
    if request.method == "POST":
        return controller.search_tips_by_title(request.method)
    return controller.search_tips_by_title(request.method)


@app.route("/check", methods=["POST"])
def check_url():
    return controller.check_url(request.get_data().decode("UTF-8"))


@app.route("/toggle/<int:tip_id>")
def toggle_read(tip_id):
    return controller.toggle_read(tip_id)
