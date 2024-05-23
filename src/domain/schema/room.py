from typing import Optional

from pydantic import BaseModel, ConfigDict


class RoomSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int] = None
    room_name: str
    room_number: int
    info: str
    project_id: int
