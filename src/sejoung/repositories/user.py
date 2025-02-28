from sqlalchemy.orm import Session

from sejoung.entities.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id) -> User:
        return self.db.get(User, user_id)
