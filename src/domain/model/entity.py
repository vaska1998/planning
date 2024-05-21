import uuid
from datetime import datetime
from typing import TypeVar

from sqlalchemy.orm import Mapped, mapped_column, declarative_base

Base = declarative_base()


class AppEntity(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[float] = mapped_column(default=datetime.now().timestamp())
    updated_at: Mapped[float] = mapped_column(default=datetime.now().timestamp(), onupdate=datetime.now().timestamp())

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"