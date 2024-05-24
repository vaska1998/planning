from typing import List

from sqlalchemy.orm import mapped_column, Mapped, relationship


from src.domain.model.entity import AppEntity
from src.domain.model.room import Room


class Project(AppEntity):
    __tablename__ = 'projects'

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rooms: Mapped[List["Room"]] = relationship()


