import uuid

from pydantic import BaseModel, ConfigDict


class ProjectSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    description: str

