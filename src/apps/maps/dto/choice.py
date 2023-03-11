from pydantic import BaseModel

from apps.maps.dto.place import PlaceDto
from apps.maps.dto.transport import TransportTypeDto
from apps.maps.dto.travel_time import TravelTimeDto


class ChoiceDto(BaseModel):
    id: int
    transport: TransportTypeDto
    travel_time: TravelTimeDto
    place: PlaceDto
