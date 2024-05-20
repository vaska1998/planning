from sqlalchemy.orm import mapped_column, Mapped

from src.domain.model.entity import AppEntity


class Project(AppEntity):
    __tablename__ = 'project'

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
