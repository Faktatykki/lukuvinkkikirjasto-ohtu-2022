# from app import app
# import data.db as db
from data import db

def get_all_tips() -> list:
    '''kutsuu data-layeria ja saa vastaukseksi tietokannasta löytyvät vinkit'''
    
    tips = db.get_all_tips()

    return tips


def add_tip(title: str, url: str) -> bool:
    """
        passaa eteenpäin käyttöliittymästä saadut parametrit uuden vinkin lisäämiseksi data-layerille.
        Tarkistetaan myös että parametrit eivät ole tyhjiä (myös välilyöntien varalta)
    """

    if not title.strip() or not url.strip():
        return False

    return db.add_tip(title, url)
