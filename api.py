from fastapi import FastAPI

from src.application.service.project import ProjectService
from src.domain.schema.project import ProjectSchema
from src.interface.cli._injector import injector

app = FastAPI()


@app.get("/project/")
def get_all_projects():
    application = injector.get(ProjectService)
    projects = application.get_all_projects
    return projects


@app.get("/project/{id}")
def get_project(id):
    application = injector.get(ProjectService)
    project = application.get_project(id)
    return project


@app.post("/project/")
def create_project(project: ProjectSchema):
    application = injector.get(ProjectService)
    application.project_repository.add(project)

