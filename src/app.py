from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "Hello world! :)"

@app.route("/1")
def page1():
    return "What's up? :)"

@app.route("/2")
def page2():
    return "Hi there! :)"

@app.route("/test")
def page3():
    result = db.session.execute("SELECT content FROM test")
    contents = result.fetchall()
    return contents

