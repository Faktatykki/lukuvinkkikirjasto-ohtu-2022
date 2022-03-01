from os import getenv
from flask import Flask, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy
import logic.app_logic as logic

app = Flask(__name__)
# Has to defined, but will be overwritten by the Heroku config variables.
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/mainpage")
def browse_tips():
    '''Näyttää pääsivun jossa näkyy tietokannasta löytyvät vinkit ja lomake jolla lisätä uusi'''
    tips = logic.get_all_tips()

    return render_template("main_page.html", tips=tips)


@app.route("/add", methods=["POST"])
def add_tip():
    """Tekee post-pyynnön käyttäen lomakkeesta saatuja parametreja,
        eli lähettää uuden vinkin kutsuen logic-layerin add_tip-funktiota, joka palauttaa boolean arvon.
        Jos palauttaa True, niin vinkki lisättiin tietokantaan, jos False, niin jotain meni pieleen.
     """
    title = request.form["title"]
    url = request.form["url"]

    success = logic.add_tip(title, url)

    if success:
        return redirect("/mainpage")

    print("Something went wrong")
    return redirect("/mainpage")



@app.route("/")
def index():
    '''Ohjaa pääsivulle'''
    return redirect("/mainpage")
