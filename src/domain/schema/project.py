import uuid
from dataclasses import Field
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ProjectSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    name: str
    description: str


