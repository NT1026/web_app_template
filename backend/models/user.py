from sqlalchemy.orm import Mapped, relationship
from typing import Optional

from models.base import Base, BaseType


class User(Base):
    __tablename__ = "User"
    uid: Mapped[BaseType.uid]
    password: Mapped[BaseType.hashed_password]
    name: Mapped[BaseType.str_20]

    def __init__(self, uid: str, password: str, name: str) -> None:
        self.uid = uid
        self.password = password
        self.name = name

    def __repr__(self) -> str:
        return f"User(uid={self.uid}, password={self.password}, name={self.name})"
