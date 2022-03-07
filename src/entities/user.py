class User():
    def __init__(self, user_id, username, admin=False) -> None:
        self.user_id = user_id
        self.username = username
        self.admin = admin
