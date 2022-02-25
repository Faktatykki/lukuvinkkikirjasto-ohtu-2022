from flask import redirect, request, render_template

from app import app

from logic import logic


@app.route("/mainpage")
def browse_tips():
    tips = logic.get_all_tips()

    return render_template("main_page.html", tips = tips)