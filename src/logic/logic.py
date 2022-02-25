from app import app
from data import db


def get_all_tips():
    tips = db.get_all_tips()

    return tips