from sqlalchemy.orm import Session
from models import User
from models.user import UserSchema
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
    
    def get_by_id(self, user_id:str) -> UserSchema | None:
        user = self.db.query(User).filter(User.id == user_id).first()
        if user is None:
            return None
        return UserSchema.model_validate(user, from_attributes=True)