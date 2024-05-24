from abc import ABC
from injector import inject

from src.domain.model.project import Room
from src.infrastructure.repository.alchemy.base import AlchemyRepository
from src.infrastructure.repository.alchemy.engine import AlchemyEngine


class RoomRepository(AlchemyRepository[Room], ABC):
    @inject
    def __init__(self, engine: AlchemyEngine):
        super().__init__(engine, Room)
