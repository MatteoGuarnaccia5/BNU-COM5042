'''Schema for user'''
from typing import Optional

from pydantic import BaseModel

# pylint: disable=too-few-public-methods
class UserSchema(BaseModel):
    '''User schema'''
    id: int
    name: str
    email: str
    password: str
    dob: Optional[int]
