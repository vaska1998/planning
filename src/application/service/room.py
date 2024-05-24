from typing import List

from src.domain.repository.base import AppQuery, AppFilter
from src.domain.schema.room import RoomSchema
from src.infrastructure.logger.app_logger import AppLogger
from src.infrastructure.repository.alchemy.room import RoomRepository
from injector import inject
from src.domain.model.room import Room


class RoomService:
    room_repository: RoomRepository
    logger: AppLogger

    @inject
    def __init__(self, room_repository: RoomRepository, logger: AppLogger):
        self.room_repository = room_repository
        self.logger = logger

    def create_room(self, room: Room):
        self.room_repository.add(room)

    def show_all_rooms(self) -> List[RoomSchema]:
        rooms = self.room_repository.get_all()
        return [RoomSchema.model_validate(room) for room in rooms]

    def show_room(self, room_id: int) -> RoomSchema:
        room = self.room_repository.get(room_id)
        return RoomSchema.model_validate(room)

    def delete_room(self, room_id: int):
        room = self.room_repository.get(room_id)
        self.room_repository.delete(room)

    def delete_all_rooms_by_project_id(self, project_id: int):
        query = AppQuery(
            filters=[AppFilter.create(lambda x: x.project_id == project_id)]
        )
        rooms = self.room_repository.find(query)
        for room in rooms:
            self.delete_room(room.id)
