import requests
from data.db import DBManager
from lxml.html import fromstring

class AppLogic:
    def __init__(self, db: DBManager):
        self.db = db

    def get_all_tips(self) -> list:
        '''kutsuu data-layeria ja saa vastaukseksi tietokannasta löytyvät vinkit'''
        tips = self.db.get_all_tips()
        return tips

    def search_tips_by_title(self, title: str) -> list:
        '''Kutsuu data-layerin metodia josta palauttaa listan tuloksia tietokannasta. Palauttaa tyhjän listan jos parametri on tyhjä'''
        if not title.strip():
            return []

        return self.db.get_tips_by_title(title)

    def add_tip(self, title: str, url: str, username: str = '') -> bool:
        """
            passaa eteenpäin käyttöliittymästä saadut parametrit uuden vinkin lisäämiseksi data-layerille.
            Tarkistetaan myös että parametrit eivät ole tyhjiä (myös välilyöntien varalta)
        """
        if not title or not url or not title.strip() or not url.strip():
            return False
        if username != '':
            return self.db.add_tip(title, url, username)
        return self.db.add_tip(title, url)

    def check_url(self, url: str) -> int:
        '''ottaa parametrina urlin, tarkistaa requests-kirjaston avulla että saako yhteyden. Jos onnistuu, niin palauttaa sivun titlen.'''
        title = None
        if "https://" not in url:
            url = "https://" + url
        status_code = 404
        req = None
        try:
            req = requests.get(url)
            status_code = req.status_code
        except Exception as exception:
            print(exception)
        if req:
            title = fromstring(req.content).findtext(".//title")
            if title and title != "":
                return title
        return status_code