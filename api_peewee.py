from fastapi import FastAPI

from src.application.service.peewee_project import PeeweeProjectService
from src.application.service.peewee_room import PeeweeRoomService
from src.domain.model.peewee_project import Project
from src.domain.model.peewee_room import Room
from src.domain.schema.project import ProjectSchema
from src.domain.schema.room import RoomSchema
from src.interface.cli._injector import injector

app = FastAPI()

@app.get("/project/")
def get_all_projects():
    application = injector.get(PeeweeProjectService)
    projects = application.get_all_projects()
    return projects


@app.get("/project/{id}")
def get_project(id: int):
    application = injector.get(PeeweeProjectService)
    project = application.get_one_project(id)
    return project


@app.post("/project/")
def create_project(project: ProjectSchema):
    application = injector.get(PeeweeProjectService)
    print(project)
    application.create_project(project)


@app.delete("/project/{id}")
def delete_project(id: int):
    application = injector.get(PeeweeProjectService)
    application.delete_project(id)


@app.get("/rooms")
def get_all_rooms():
    application = injector.get(PeeweeRoomService)
    rooms = application.show_all_rooms()
    return rooms


@app.get("/room/{id}")
def get_room(id: int):
    application = injector.get(PeeweeRoomService)
    room = application.show_room(id)
    return room


@app.post("/room/")
def create_room(room: RoomSchema):
    application = injector.get(PeeweeRoomService)
    new_room = Room(room_name=room.room_name,
                    project_id=room.project_id,
                    room_number=room.room_number,
                    info=room.info
                    )
    application.create_room(new_room)


@app.delete("/room/{id}")
def delete_room(id: int):
    application = injector.get(PeeweeRoomService)
    application.delete_room(id)


@app.post('/roomsAll/{project_id}')
def delete_all_rooms(project_id: int):
    application = injector.get(PeeweeRoomService)
    application.delete_all_rooms_by_project_id(project_id)