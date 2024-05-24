from abc import ABC
from injector import inject
from src.domain.model.peewee_room import Room
from src.infrastructure.repository.peewee.base import PeeweeRepository
from src.infrastructure.repository.peewee.engine import PeeweeEngine


class RoomPeeweeRepository(PeeweeRepository[Room], ABC):
    @inject
    def __init__(self, engine: PeeweeEngine):
        super().__init__(engine, Room)
