from typing import Optional

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str
    name: str

    def __repr__(self):
        return f"<User(id={self.id}, " \
               f"user_id=\"{self.user_id}\", " \
               f"name=\"{self.name}\")>"
