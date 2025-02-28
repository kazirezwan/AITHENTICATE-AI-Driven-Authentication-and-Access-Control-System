import json
import hashlib
from encryption import AESCipher

class AuthSystem:
    def __init__(self, user_file, encryption_key):
        self.user_file = user_file
        self.encryption_key = encryption_key
        self.cipher = AESCipher(encryption_key)

    def load_users(self):
        try:
            with open(self.user_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_users(self, users):
        with open(self.user_file, 'w') as f:
            json.dump(users, f)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        users = self.load_users()
        if username in users:
            return "User  already exists."
        hashed_password = self.hash_password(password)
        users[username] = hashed_password
        self.save_users(users)
        return "User  registered successfully."

    def authenticate_user(self, username, password):
        users = self.load_users()
        hashed_password = self.hash_password(password)
        if username in users and users[username] == hashed_password:
            return True
        return False

    def access_control(self, username):
        # Implement your access control logic here
        return f"Access granted to {username}."