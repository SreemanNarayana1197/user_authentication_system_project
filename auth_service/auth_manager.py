import bcrypt
from auth_service.database import UserDatabase

class AuthManager:
    def __init__(self, db: UserDatabase):
        self.db = db

    def register_user(self, username: str, password: str) -> bool:
        if self.db.get_user(username) is not None:
            print("User already exists.")
            return False
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.db.add_user(username, hashed_password)
        print("User registered successfully.")
        return True

    def authenticate_user(self, username: str, password: str) -> bool:
        user = self.db.get_user(username)
        if user is None:
            print("User not found.")
            return False
        if bcrypt.checkpw(password.encode(), user['password']):
            print("Authentication successful.")
            return True
        else:
            print("Incorrect password.")
            return False
            