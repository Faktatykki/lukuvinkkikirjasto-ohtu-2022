from data.db import DBManager


class AppLogic:
    def __init__(self, db: DBManager):
        self.db = db

    def get_all_tips(self) -> list:
        '''kutsuu data-layeria ja saa vastaukseksi tietokannasta löytyvät vinkit'''
        tips = self.db.get_all_tips()
        print('----- tips in app_logic.get_all_tips: ', tips)
        return tips

    def search_tips_by_title(self, title: str) -> list:
        '''Kutsuu data-layerin metodia josta palauttaa listan tuloksia tietokannasta. Palauttaa tyhjän listan jos parametri on tyhjä'''
        if not title.strip():
            return []

        return self.db.get_tips_by_title(title)

    def add_tip(self, title: str, url: str) -> bool:
        """
            passaa eteenpäin käyttöliittymästä saadut parametrit uuden vinkin lisäämiseksi data-layerille.
            Tarkistetaan myös että parametrit eivät ole tyhjiä (myös välilyöntien varalta)
        """
        if not title or not url or not title.strip() or not url.strip():
            return False
        return self.db.add_tip(title, url)
