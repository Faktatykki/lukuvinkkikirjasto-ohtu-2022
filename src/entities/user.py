class User():
    def __init__(self, id, username, admin=False) -> None:
        self.id=id
        self.username=username
        self.admin=admin