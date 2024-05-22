from fastapi import FastAPI

from src.application.service.peewee_project import PeeweeProjectService
from src.domain.model.peewee_project import Project
from src.domain.schema.project import ProjectSchema
from src.interface.cli._injector import injector

app = FastAPI()

@app.get("/project/")
def get_all_projects():
    application = injector.get(PeeweeProjectService)
    projects = application.get_all_projects()
    return projects


@app.get("/project/{id}")
def get_project(id:int):
    application = injector.get(PeeweeProjectService)
    project = application.get_one_project(id)
    return project


@app.post("/project/")
def create_project(project: ProjectSchema):
    application = injector.get(PeeweeProjectService)
    print(project)
    application.create_project(project)


@app.delete("/project/{id}")
def delete_project(id:int):
    application = injector.get(PeeweeProjectService)
    application.delete_project(id)
