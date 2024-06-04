from datetime import datetime
from typing import List
from src.domain.model.peewee_room import Room
from src.domain.repository.base import AppQuery, AppFilter
from src.domain.schema.room import RoomSchema
from src.infrastructure.logger.app_logger import AppLogger
from injector import inject

from src.infrastructure.repository.peewee.room import RoomPeeweeRepository


class PeeweeRoomService:
    room_repository = RoomPeeweeRepository
    logger: AppLogger

    @inject
    def __init__(self, room_repository: RoomPeeweeRepository, logger: AppLogger):
        self.room_repository = room_repository
        self.logger = logger

    def create_room(self, room: RoomSchema):
        time = datetime.now().timestamp()
        new_room = Room(room_name=room.room_name,
                        project_id=room.project_id,
                        room_number=room.room_number,
                        info=room.info,
                        created_at=time,
                        updated_at=time,
                        )
        self.room_repository.add(new_room)

    def show_all_rooms(self):
        rooms = self.room_repository.get_all()
        result = []
        for room in rooms:
            result.append(RoomSchema(
                id=room.id,
                room_number=room.room_number,
                room_name=room.room_name,
                info=room.info,
                project_id=room.project_id.id
            ))

        return result

    def show_room(self, room_id: int):
        room = self.room_repository.get(room_id)
        result = RoomSchema(
            id=room.id,
            room_number=room.room_number,
            room_name=room.room_name,
            info=room.info,
            project_id=room.project_id.id
        )
        return result

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
