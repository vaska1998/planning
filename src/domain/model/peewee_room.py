from peewee import IntegerField, CharField, ForeignKeyField

from src.domain.model.peewee_project import Project
from src.domain.model.peewwee_entity import PeeweeEntity


class Room(PeeweeEntity):
    room_number: int = IntegerField()
    room_name: str = CharField()
    info: str = CharField()
    project_id: int = ForeignKeyField(Project, backref='rooms')

    class Meta:
        db_table = 'rooms'
