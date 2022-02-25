from flask import redirect, request, render_template

from app import app

import logic.appLogic as logic


@app.route("/mainpage")
def browse_tips():
    '''Näyttää pääsivun jossa näkyy tietokannasta löytyvät vinkit ja lomake jolla lisätä uusi'''
    tips = logic.get_all_tips()

    return render_template("main_page.html", tips = tips)

#if add_tip returns false, maybe some warning?
@app.route("/add", methods = ["POST"])
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
    else:
        print("Something went wrong")

    return redirect("/mainpage")

