from flask import redirect, request, render_template
from app import app
import logic.app_logic as logic
from logic.user_logic import signup


@app.route("/mainpage")
def browse_tips():
    '''Näyttää pääsivun jossa näkyy tietokannasta löytyvät vinkit ja lomake jolla lisätä uusi'''
    tips = logic.get_all_tips()

    return render_template("main_page.html", tips=tips)

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
def signup():
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
    if signup(username, password1):
        return redirect("/mainpage")
    return render_template("error.html", message="Käyttäjänimi on jo käytössä")
