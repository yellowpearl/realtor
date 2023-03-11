from pydantic import BaseModel


class PlaceDto(BaseModel):
    id: int
    name: str
