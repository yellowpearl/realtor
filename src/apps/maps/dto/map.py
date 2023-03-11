import uuid
from typing import List

from pydantic import BaseModel

from apps.maps.dto.choice import ChoiceDto


class MapDto(BaseModel):
    unique_id: uuid.UUID
    email: str
    choices: List[ChoiceDto]
