from flask import Flask

app = Flask(__name__)

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
    return "testing..."