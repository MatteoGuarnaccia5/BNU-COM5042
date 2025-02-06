from typing import Optional
from pydantic import BaseModel
from database.database import Database

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    password: str
    dob: Optional[int]


class User:
    
    def __init__(self) -> None:
        self._database = Database()


    def get(self, user_id: int) -> UserSchema:
        result = self._database.getUser(id=user_id)
        if result is None:
            raise ValueError
        
        return result
    
    def authenticate(self, email: str, password: str) -> int:
        result = self._database.authenticate_user(email, password)
        if result is None:
            raise ValueError
        
        return result