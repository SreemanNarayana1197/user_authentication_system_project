# User Authentication System

This project is a basic user authentication system built in Python, demonstrating user registration, password hashing, and authentication.

## Setup Instructions

1. Install dependencies:
    ```bash
    pip install bcrypt
    ```

2. Run the authentication service:
    ```bash
    python main.py
    ```

## Project Structure

- `auth_service/`: Contains core logic for registration and authentication.
- `main.py`: The main entry point to register and authenticate users.

## Note
In a real deployment, consider replacing the in-memory `UserDatabase` with a proper database.
        