from peewee import CharField

from src.domain.model.peewwee_entity import PeeweeEntity


class Project(PeeweeEntity):
    name: str = CharField()
    description: str = CharField()

    class Meta:
        db_table = 'projects'
