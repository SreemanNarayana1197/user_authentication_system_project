class UserDatabase:
    def __init__(self):
        # Simulate a database with an in-memory dictionary
        self.users = {}

    def add_user(self, username: str, hashed_password: bytes):
        self.users[username] = {"password": hashed_password}

    def get_user(self, username: str):
        return self.users.get(username)
            