"""Database module to interact directly with database"""

import json

from smart_home_app.schemas.user import UserSchema


class Database:
    """Database class to interact with database"""

    def __init__(self) -> None:
        self.data = self.load_data()

    def load_data(self):
        """Load data from database"""
        try:
            # pylint: disable=unspecified-encoding
            with open("./database.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def get_user(self, u_id: int) -> UserSchema | None:
        """Get user document"""
        for user in self.data:
            if user["id"] == u_id:
                return UserSchema(**user)
        return None

    def authenticate_user(self, email: str, password: str) -> int | None:
        """Authenticate user"""
        for user in self.data:
            if user["email"] == email and user["password"] == password:
                return user["id"]
        return None

    def save_data(self) -> None:
        """Save database"""
        # pylint: disable=unspecified-encoding
        with open("./database.json", "w") as file:
            json.dump(self.data, file)

        # Reload data
        self.data = self.load_data()

    def create_user(self, user: UserSchema) -> None:
        """Insert document into database"""

        for u in self.data:
            if u["email"] == user.email:
                raise ValueError("User already exists")

        self.data.append(user.model_dump())
        self.save_data()
