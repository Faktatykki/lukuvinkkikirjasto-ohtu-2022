from flask import redirect, request, render_template, session
from sqlalchemy.exc import IntegrityError
from app import app
import logic.app_logic as logic
from logic.user_logic import signup, signin
from entities.user import User


@app.route("/mainpage")
def browse_tips():
    '''Näyttää pääsivun jossa näkyy tietokannasta löytyvät vinkit ja lomake jolla lisätä uusi'''
    tips = logic.get_all_tips()
    if 'username' in session:
        return render_template("main_page.html", tips=tips, username=session["username"])
    return render_template("main_page.html", tips=tips, username=None)
     
# if add_tip returns false, maybe some warning?


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


@app.route("/signup", methods=["POST"])
def add_new_user():
    """Käsittelee uuden käyttäjän luonnin."""
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if len(username) < 2 or len(username) > 20:
        return render_template(
            "error.html", message="Käyttäjänimen tulee olla 2-20 merkkiä pitkä"
        )
    if len(password1) < 2 or len(password1) > 20:
        return render_template(
            "error.html", message="Salasanan tulee olla 2-20 merkkiä pitkä"
        )
    if password1 != password2:
        return render_template("error.html", message="Salasanat eivät täsmää.")
    response=signup(username, password1)
    if isinstance(response, User):
        session["username"] = username
        return redirect("/mainpage")
    if isinstance(response, IntegrityError):
        return render_template("error.html", message="Käyttäjänimi on varattu.")
    return render_template("error.html", message=response)


@app.route("/signup", methods=["GET"])
def get_signup_page():
    """Palauttaa signup-sivun"""
    return render_template("signup.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    logged_in_user = signin(username, password)
    if isinstance(logged_in_user, User):
        session["username"] = username
        return redirect("/mainpage")
    return render_template("error.html", message="Väärä käyttäjä tai salasana")

@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/mainpage")
