from flask import render_template

class AppLogic:
    def __init__(self, db):
        self.db = db

    def get_all_tips(self) -> list:
        '''kutsuu data-layeria ja saa vastaukseksi tietokannasta löytyvät vinkit'''
        tips = self.db.get_all_tips()
        return tips

    def add_tip(self, title: str, url: str) -> bool:
        """
            passaa eteenpäin käyttöliittymästä saadut parametrit uuden vinkin lisäämiseksi data-layerille.
            Tarkistetaan myös että parametrit eivät ole tyhjiä (myös välilyöntien varalta)
        """
        if not title.strip() or not url.strip():
           return False
        return self.db.add_tip(title, url)

