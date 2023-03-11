from pydantic import BaseModel


class TravelTimeDto(BaseModel):
    id: int
    time: str
