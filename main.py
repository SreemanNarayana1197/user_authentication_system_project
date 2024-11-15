from auth_service.auth_manager import AuthManager
from auth_service.database import UserDatabase

def main():
    # Initialize the simulated database and authentication manager
    db = UserDatabase()
    auth_manager = AuthManager(db)

    # Register a new user
    username = "test_user"
    password = "secure_password"
    auth_manager.register_user(username, password)

    # Attempt to authenticate the registered user
    auth_manager.authenticate_user(username, password)

    # Attempt to authenticate with an incorrect password
    auth_manager.authenticate_user(username, "wrong_password")

if __name__ == "__main__":
    main()
        