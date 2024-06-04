from injector import Module, singleton

from src.application.service.peewee_project import PeeweeProjectService
from src.application.service.peewee_room import PeeweeRoomService
from src.application.service.project import ProjectService
from src.application.service.room import RoomService
from src.infrastructure.config.app_config import AppConfig
from src.infrastructure.logger.app_logger import AppLogger
from src.infrastructure.repository.alchemy.engine import AlchemyEngine
from src.infrastructure.repository.alchemy.project import ProjectRepository
from src.infrastructure.repository.alchemy.room import RoomRepository
from src.infrastructure.repository.peewee.engine import PeeweeEngine
from src.infrastructure.repository.peewee.project import ProjectPeeweeRepository
from src.infrastructure.repository.peewee.room import RoomPeeweeRepository


class AppModule(Module):
    config: AppConfig

    def __init__(self, config: AppConfig):
        self.config = config

    def configure(self, binder):
        # config
        binder.bind(AppConfig, self.config, scope=singleton)

        # logger
        binder.bind(AppLogger, to=AppLogger, scope=singleton)

        # repositories
        binder.bind(AlchemyEngine, AlchemyEngine)
        binder.bind(PeeweeEngine, PeeweeEngine)
        binder.bind(ProjectRepository, to=ProjectRepository)
        binder.bind(ProjectPeeweeRepository, to=ProjectPeeweeRepository)
        binder.bind(RoomRepository, to=RoomRepository)
        binder.bind(RoomPeeweeRepository, to=RoomPeeweeRepository)

        # services
        binder.bind(ProjectService, ProjectService, scope=singleton)
        binder.bind(PeeweeProjectService, PeeweeProjectService, scope=singleton)
        binder.bind(RoomService, to=RoomService, scope=singleton)
        binder.bind(PeeweeRoomService, PeeweeRoomService, scope=singleton)
