from apps.maps.dto.choice import ChoiceDto
from apps.maps.dto.map import MapDto
from apps.maps.dto.request import RequestChoiceDto
from apps.maps.factory.choice import ChoiceFactory
from apps.maps.models.choice import Choice
from apps.maps.models.map import Map
from apps.maps.models.place import Place
from apps.maps.models.transport import TransportType
from apps.maps.models.travel_time import TravelTime


class ChoiceRepository:

    def __init__(self):
        self.model = Choice
        self.map_model = Map
        self.travel_time_model = TravelTime
        self.transport_model = TransportType
        self.place_model = Place
        self.factory = ChoiceFactory()

    def create(self, map: MapDto, choice: RequestChoiceDto) -> ChoiceDto:
        map = self.map_model.objects.get(unique_id=map.unique_id)
        travel_time = self.travel_time_model.objects.get(time=choice.travel_time)
        transport = self.transport_model.objects.get(name=choice.transport)
        place = self.place_model.objects.get(name=choice.place)
        item = self.model.objects.create(
            map=map,
            transport=transport,
            place=place,
            travel_time=travel_time
        )
        return self.factory.dto_from_model(item)
