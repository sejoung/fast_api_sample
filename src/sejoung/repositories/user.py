from typing import Type

from sqlalchemy.orm import Session

from sejoung.entities.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id) -> Type[User] | None:
        return self.db.query(User).filter(User.id == user_id).first()
