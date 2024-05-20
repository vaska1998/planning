from injector import Module, singleton

from src.application.service.project import ProjectService
from src.infrastructure.config.app_config import AppConfig
from src.infrastructure.logger.app_logger import AppLogger
from src.infrastructure.repository.alchemy.engine import AlchemyEngine
from src.infrastructure.repository.alchemy.project import ProjectRepository


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
        binder.bind(ProjectRepository, to=ProjectRepository, scope=singleton)

        # services
        binder.bind(ProjectService, ProjectService, scope=singleton)
