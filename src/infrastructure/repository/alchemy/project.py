from abc import ABC

from injector import inject

from src.domain.model.project import Project
from src.infrastructure.repository.alchemy.base import AlchemyRepository
from src.infrastructure.repository.alchemy.engine import AlchemyEngine


class ProjectRepository(AlchemyRepository[Project], ABC):
    @inject
    def __init__(self, engine: AlchemyEngine):
        super().__init__(engine, Project)
