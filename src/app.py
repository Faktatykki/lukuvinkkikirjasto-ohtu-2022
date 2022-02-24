from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
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

