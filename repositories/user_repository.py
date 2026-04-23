from sqlalchemy.orm import Session
from models import User
from repositories.abstract_repository import AbstractRepository


class UserRepository(AbstractRepository):
    def create(self, email:str, password:str):
        user = User(
            email=email,
            password=password
        )
        self.db.add(user)
        self.db.commit()

    def get_by_email(self, email:str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()
    