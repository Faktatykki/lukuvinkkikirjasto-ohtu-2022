from flask import redirect, request, render_template, session
from sqlalchemy.exc import IntegrityError
from os import getenv
from logic.app_logic import AppLogic
from logic.user_logic import UserLogic
from entities.user import User
from data.db import DBManager


class Controller:
    def __init__(self, app=False):
        self.db = DBManager(app=app)
        self.app_logic = AppLogic(self.db)
        self.user_logic = UserLogic(self.db)
        if getenv("DEV_ENVIRON"):
            self.session = {}
        else:
            self.session = session

    def browse_tips(self):
        '''Näyttää pääsivun jossa näkyy tietokannasta löytyvät vinkit ja lomake jolla lisätä uusi'''
        titles = getenv("TIPS_TABLE_COLUMNS").split(",")
        for i in range(len(titles)):
            titles[i] = titles[i].split(";")[0]
        tips = [titles]
        tips += self.app_logic.get_all_tips()
        if 'username' in self.session:
            return render_template("main_page.html", tips=tips, username=self.session["username"])
        return render_template("main_page.html", tips=tips, username=None)

    def add_tip(self):
        title = request.form["title"]
        url = request.form["url"]
        if self.app_logic.add_tip(title, url):
            return redirect("/")
        print("Something went wrong")
        return redirect("/")

    # maybe refactor so that functionality is moved to app_logic_class and user_logic is made into a class
    def add_new_user(self):
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
        # (see above comment) because this self.app_logic.db isn't great
        response = self.user_logic.signup(username, password1)
        if isinstance(response, User):
            self.session["username"] = username
            return redirect("/")
        if isinstance(response, IntegrityError):
            return render_template("error.html", message="Käyttäjänimi on varattu.")
        return render_template("error.html", message=response)

    def get_signup_page(self):
        """Palauttaa signup-sivun"""
        return render_template("signup.html")

    def login(self):
        username = request.form["username"]
        password = request.form["password"]
        logged_in_user = self.user_logic.signin(username, password)
        if isinstance(logged_in_user, User):
            self.session["username"] = username
            return redirect("/")
        return render_template("error.html", message="Väärä käyttäjä tai salasana")

    def login_page(self):
        return render_template("login.html")

    def logout(self):
        self.session.pop("username", None)
        return redirect("/")
