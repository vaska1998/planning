import uuid
from typing import List

from injector import inject

from src.domain.model.project import Project
from src.domain.schema.project import ProjectSchema
from src.infrastructure.logger.app_logger import AppLogger
from src.infrastructure.repository.alchemy.project import ProjectRepository


class ProjectService:
    project_repository: ProjectRepository
    logger: AppLogger

    @inject
    def __init__(self, project_repository: ProjectRepository, logger: AppLogger):
        self.project_repository = project_repository
        self.logger = logger

    def get_all_projects(self) -> List[ProjectSchema]:
        projects = self.project_repository.get_all()
        return [ProjectSchema.model_validate(project) for project in projects]

    def get_one_project(self, project_id: uuid.UUID) -> ProjectSchema:
        project = self.project_repository.get(project_id)
        return ProjectSchema.model_validate(project)

    def create_project(self, project: ProjectSchema):
        self.project_repository.add(project)
