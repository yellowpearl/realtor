from apps.maps.dto.map import MapDto
from apps.maps.dto.request import RequestChoiceDto
from apps.maps.repository.choice import ChoiceRepository


class ChoiceService:
    def __init__(self):
        self.repository = ChoiceRepository()

    def create_choice_for_map(self, map: MapDto, choice: RequestChoiceDto):
        self.repository.create(map, choice)