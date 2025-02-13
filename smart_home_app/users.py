'''Module for the user class'''
from smart_home_app.database.database import Database
from smart_home_app.schemas.user import UserSchema


class User:
    '''The User class'''
    def __init__(self) -> None:
        self._database = Database()


    def get(self, user_id: int) -> UserSchema:
        '''Get user'''
        result = self._database.get_user(u_id=user_id)
        if result is None:
            raise ValueError

        return result

    def authenticate(self, email: str, password: str) -> int:
        '''Authenticate user'''
        result = self._database.authenticate_user(email, password)
        if result is None:
            raise ValueError

        return result

    def create(self, user: UserSchema) -> None:
        '''Create users'''
        self._database.create_user(user)
