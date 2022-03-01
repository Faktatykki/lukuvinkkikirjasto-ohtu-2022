# from app import app
import data.db as db

def get_all_tips() -> list:
    '''kutsuu data-layeria ja saa vastaukseksi tietokannasta löytyvät vinkit'''
    tips = db.get_all_tips()
    return tips

def add_tip(title: str, url: str) -> bool:
    '''passaa eteenpäin käyttöliittymästä saadut parametrit uuden vinkin lisäämiseksi data-layerille'''
    return db.add_tip(title, url)
