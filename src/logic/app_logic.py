import requests
from data.db import DBManager
from lxml.html import fromstring


class AppLogic:
    def __init__(self, db: DBManager):
        self.db = db

    def get_all_tips(self, user_id: int = 0) -> list:
        '''kutsuu data-layeria ja saa vastaukseksi tietokannasta löytyvät vinkit'''
        return self.db.get_all_tips(user_id)

    def search_tips_by_title(self, title: str) -> list:
        """Hakee data-kerrokselta parametria vastaavia vinkkejä

        Args:
            title (str): Haettava teksti

        Returns:
            list: Hakuehtoa vastaavat vinkit.
                Palauttaa tyhjän listan, jos vinkkejä ei löydy, tai jos haettava teksti on tyhjä
        """
        if not title.strip():
            return []

        return self.db.get_tips_by_title(title)

    def add_tip(self, title: str, url: str, username: str = '') -> bool:
        """Lähettää käyttöliittymästä saadut parametrit data-kerrokselle

        Args:
            title (str): Lisättävän vinkin otsikko
            url (str): Lisättävän vinkin osoite
            username (str, optional): Kirjautuneen käyttäjän käyttäjänimi. Kirjautumattomalla ''

        Returns:
            bool: Onnistunut lisäys palauttaa True, muutoin False
        """
        if not title or not url or not title.strip() or not url.strip():
            return False
        if username != '':
            return self.db.add_tip(title, url, username)
        return self.db.add_tip(title, url)

    def check_url(self, url: str) -> int:
        '''ottaa parametrina urlin, tarkistaa requests-kirjaston avulla että saako yhteyden. Jos onnistuu, niin palauttaa sivun titlen.'''
        req_data = url
        title = None
        schema = ""
        if "https://" not in url:
            schema = "https://"
        final_url = schema + req_data
        status_code = 404
        req = None
        try:
            req = requests.get(final_url)
            status_code = req.status_code
        except Exception as exception:
            print(exception)
        if req:
            title = fromstring(req.content).findtext(".//title")
            if title and title != "":
                return title
        return status_code

    def toggle_read(self, tip_id: int, user_id: int) -> bool:
        self.db.toggle_read(tip_id, user_id)
        return True
