from abc import ABC

from injector import inject

from src.domain.model.peewee_project import Project
from src.infrastructure.repository.peewee.base import PeeweeRepository
from src.infrastructure.repository.peewee.engine import PeeweeEngine


class ProjectPeeweeRepository(PeeweeRepository[Project], ABC):
    @inject
    def __init__(self, engine: PeeweeEngine):
        super().__init__(engine, Project)
