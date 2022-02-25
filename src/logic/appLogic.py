from app import app
import data.db as db


def get_all_tips():
    tips = db.get_all_tips()

    return tips