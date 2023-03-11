from pydantic import BaseModel


class TransportTypeDto(BaseModel):
    id: int
    name: str
