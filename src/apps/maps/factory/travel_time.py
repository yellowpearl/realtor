from apps.maps.dto.travel_time import TravelTimeDto
from apps.maps.models.travel_time import TravelTime


class TravelTimeFactory:

    def __init__(self):
        self.dto = TravelTimeDto

    def dto_from_model(self, item: TravelTime) -> TravelTimeDto:
        return self.dto(id=item.pk, time=item.time)
