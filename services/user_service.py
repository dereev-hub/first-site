from models.user import User
from repositories.user_repository import UserRepository


class UserService:
    def __init__ (self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def signup(self, email:str, password:str):
        user = self.user_repository.get_by_email(email)
        if user is not None:
            raise ValueError('Пользователь с таким имейлом уже есть')
        self.user_repository.create(email, password)

    def signin(self, email:str, password:str)->User:
        user = self.user_repository.get_by_email(email)
        if user is None:
            raise ValueError('Пользователь не найден')
        if password != user.password:
            raise ValueError('Пользователь не найден')
        return user