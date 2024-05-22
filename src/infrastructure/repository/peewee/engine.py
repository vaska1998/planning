from src.infrastructure.config.app_config import AppConfig
from injector import inject
from peewee import SqliteDatabase


class PeeweeEngine:
    database: SqliteDatabase

    @inject
    def __init__(self, app_config: AppConfig):
        self.database = SqliteDatabase(app_config.database.NAME)

    def connect(self):
        self.database.connect()

    def close(self):
        self.database.close()
