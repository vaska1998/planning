from src.domain.model.entity import AppEntity
from sqlalchemy.orm import mapped_column, Mapped

from src.domain.model.project import Project


class Room(AppEntity):
    __tablename__ = 'room'

    room_number: Mapped[int] = mapped_column(nullable=False)
    room_name: Mapped[str] = mapped_column(nullable=False)
    info: Mapped[str] = mapped_column(nullable=False)
    project_id: Mapped[int] = mapped_column(ForeignKey='project_table.id')
