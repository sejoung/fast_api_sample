from sqlalchemy import Column, String, Boolean, Integer

from sejoung.configuration.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(255))
    name = Column(String(128))
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<User(id={self.id}, " \
               f"user_id=\"{self.user_id}\", " \
               f"name=\"{self.name}\", " \
               f"is_active={self.is_active})>"
