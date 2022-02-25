from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL") # Has to defined, but will be overwritten by the Heroku config variables.
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")
def index():
    print(getenv("DATABASE_URL"))
    return "Hello world! Testing heroku deploy from github actions. Python v 3.9.10"

@app.route("/1")
def page1():
    return "What's up? :)"

@app.route("/2")
def page2():
    return "Testing heroku deploy!)"

@app.route("/test")
def test():
    result = db.session.execute("SELECT content FROM test")
    contents = result.fetchall()
    return render_template("test.html", contents=contents)

@app.route("/add", methods=["POST"])
def add():
    content = request.form["message"]
    sql = "INSERT INTO test (content) VALUES (:content)"
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return redirect("/test")
