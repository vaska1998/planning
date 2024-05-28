from peewee import IntegerField, CharField, ForeignKeyField

from src.domain.model.peewee_project import Project
from src.domain.model.peewwee_entity import PeeweeEntity


class Room(PeeweeEntity):
    room_number = IntegerField()
    room_name = CharField()
    info = CharField()
    project_id = ForeignKeyField(Project, backref='rooms')

    class Meta:
        db_table = 'rooms'
