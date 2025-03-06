import uuid

from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    name: str
    email: str


class User(UserBase, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    def __repr__(self):
        return f"<User(id={self.id}, " \
               f"email=\"{self.email}\", " \
               f"name=\"{self.name}\")>"


class UserResponse(UserBase):
    name: str
    email: str
    test: str = "test"
