import uuid

from apps.maps.dto.map import MapDto
from apps.maps.factory.request import RequestMapFactory
from apps.maps.repository.map import MapRepository
from apps.maps.service.choice import ChoiceService
from apps.user.service import UserService


class MapService:
    def __init__(self):
        self.request_map_factory = RequestMapFactory()
        self.choice_service = ChoiceService()
        self.user_service = UserService()
        self.repository = MapRepository()

    def create_from_data(self, validated_data: dict):
        request_map_dto = self.get_dto_from_validated_data(validated_data)
        self.user_service.create_from_email(request_map_dto.email)
        map = self.create_empty_map(user_email=request_map_dto.email)
        for choice in request_map_dto.choices:
            self.choice_service.create_choice_for_map(map, choice)
        self.set_paid(map.unique_id, request_map_dto.is_paid)
        return map

    def create_empty_map(self, user_email: str) -> MapDto:
        return self.repository.create(user_email)

    def set_paid(self, map_id: uuid.UUID, is_paid: bool):
        self.repository.set_paid(map_id, is_paid)

    def get_dto_from_validated_data(self, validated_data: dict):
        return self.request_map_factory.dto_from_dict(validated_data)
