from typing import List

from pydantic import BaseModel


class RequestChoiceDto(BaseModel):
    transport: str
    travel_time: int
    place: str


class RequestMapDto(BaseModel):
    choices: List[RequestChoiceDto]
    email: str
    is_paid: bool
