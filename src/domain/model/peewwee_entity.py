from datetime import datetime

from peewee import Model, AutoField, SqliteDatabase, FloatField


class PeeweeEntity(Model):
    id: int = AutoField(primary_key=True)
    created_at: float = FloatField(default=None)
    updated_at: float = FloatField(default=None)

    class Meta:
        database = SqliteDatabase('planning.db')
