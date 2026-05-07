import os

from models.user import User, UserSchema
from repositories.user_repository import UserRepository
from jwt import encode


class UserService:
    def __init__ (self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def signup(self, email:str, password:str):
        user = self.user_repository.get_by_email(email)
        if user is not None:
            raise ValueError('Пользователь с таким имейлом уже есть')
        self.user_repository.create(email, password)

    def signin(self, email:str, password:str)->str:
        user = self.user_repository.get_by_email(email)
        if user is None:
            raise ValueError('Пользователь не найден')
        if password != user.password:
            raise ValueError('Пользователь не найден')
        return self._generate_token(user.id)
    
    def _generate_token(self, user_id: int) -> str:
        payload = {
            'user_id': str(user_id)
        }
        return encode(payload, os.getenv('SECRET'), algorithm='HS256')
    
    def get_info(self, user_id: int)->UserSchema:
        return self.user_repository.get_by_id(user_id)
