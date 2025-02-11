import json
from typing import List
import numpy as np

from schemas.user import UserSchema

class Database:
    def __init__(self) -> None:
        self.data = self.loadData()

    def loadData(self):
        try:
            with open("./database.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        
    
    def getUser(self, id: int) -> UserSchema | None:
        for user in self.data:
            if user["id"] == id:
                return UserSchema(**user)

    # def listUsers(self) -> List[UserSchema]:



    def authenticate_user(self, email: str, password: str) -> int | None:
        
        for user in self.data:
            if user["email"] == email and user["password"] == password:
                return user["id"]
            
    def saveData(self) -> None:
        with open("./database.json", "w") as file:
            json.dump(self.data, file)

        # Reload data
        self.data = self.loadData()

    def createUser(self, user: UserSchema) -> None:
        self.data.append(user.model_dump())
        self.saveData()
       
