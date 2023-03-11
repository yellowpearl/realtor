from apps.maps.dto.choice import ChoiceDto
from apps.maps.factory.place import PlaceFactory
from apps.maps.factory.transport import TransportTypeFactory
from apps.maps.factory.travel_time import TravelTimeFactory
from apps.maps.models.choice import Choice


class ChoiceFactory:

    def __init__(self):
        self.dto = ChoiceDto
        self.transport_factory = TransportTypeFactory()
        self.place_factory = PlaceFactory()
        self.travel_time_factory = TravelTimeFactory()

    def dto_from_model(self, item: Choice) -> ChoiceDto:
        return self.dto(
            id=item.pk,
            transport=self.transport_factory.dto_from_model(item.transport),
            place=self.place_factory.dto_from_model(item.place),
            travel_time=self.travel_time_factory.dto_from_model(item.travel_time),
        )
