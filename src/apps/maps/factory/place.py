from apps.maps.dto.place import PlaceDto
from apps.maps.models.place import Place


class PlaceFactory:

    def __init__(self):
        self.dto = PlaceDto

    def dto_from_model(self, item: Place) -> PlaceDto:
        return self.dto(id=item.pk, name=item.name)
