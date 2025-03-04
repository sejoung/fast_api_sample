from typing import Type

from sqlalchemy.orm import Session

from sejoung.entities.user import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_user(self, user_id) -> Type[User] | None:
        return self.session.query(User).filter(User.id == user_id).first()
