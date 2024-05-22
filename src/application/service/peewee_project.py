import datetime
from typing import List

from src.domain.model.peewee_project import Project
from src.domain.schema.project import ProjectSchema
from src.infrastructure.logger.app_logger import AppLogger
from src.infrastructure.repository.peewee.project import ProjectPeeweeRepository
from injector import inject


class PeeweeProjectService:
    project_repository = ProjectPeeweeRepository
    logger: AppLogger

    @inject
    def __init__(self, project_repository: ProjectPeeweeRepository, logger: AppLogger):
        self.project_repository = project_repository
        self.logger = logger

    def get_all_projects(self) -> List[ProjectSchema]:
        projects = self.project_repository.get_all()
        return [ProjectSchema.model_validate(project) for project in projects]

    def get_one_project(self, project_id: int) -> ProjectSchema:
        project = self.project_repository.get(project_id)
        return ProjectSchema.model_validate(project)

    def create_project(self, project: ProjectSchema):
        time = datetime.datetime.now().timestamp()
        new_project = Project(
            name=project.name,
            description=project.description,
            created_at=time,
            updated_at=time,
        )
        self.project_repository.add(new_project)

    def delete_project(self, project_id: int):
        project = self.project_repository.get(project_id)
        self.project_repository.delete(project)
