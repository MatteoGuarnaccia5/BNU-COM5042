'''Schema for user'''
from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    '''User schema'''
    id: int
    name: str
    email: str
    password: str
    dob: Optional[int]
