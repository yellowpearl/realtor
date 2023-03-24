from apps.maps.dto.map import MapDto
from apps.maps.factory.choice import ChoiceFactory
from apps.maps.models.map import Map


class MapFactory:

    def __init__(self):
        self.dto = MapDto
        self.choice_factory = ChoiceFactory()

    def dto_from_model(self, item: Map) -> MapDto:

        return self.dto(
            unique_id=item.unique_id,
            email=item.user.email,
            choices=[self.choice_factory.dto_from_model(choice) for choice in item.choices.all()],
            is_paid=item.is_paid
        )
