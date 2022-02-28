# from app import app
from data.db import DBManager

class TipsLogic:
    def __init__(self, app):
        self.db = DBManager(app)

    def get_all_tips(self) -> list:
        '''Kutsuu data-layeria ja saa vastaukseksi tietokannasta löytyvät vinkit'''
        tips = self.db.get_all_tips()
        return tips

    def add_tip(self, title: str, url: str) -> bool:
        '''Passaa eteenpäin käyttöliittymästä saadut parametrit uuden vinkin lisäämiseksi data-layerille'''
        return self.db.add_tip(title, url)
