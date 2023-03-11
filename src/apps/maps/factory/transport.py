from apps.maps.dto.transport import TransportTypeDto
from apps.maps.models.transport import TransportType


class TransportTypeFactory:

    def __init__(self):
        self.dto = TransportTypeDto

    def dto_from_model(self, item: TransportType) -> TransportTypeDto:
        return self.dto(id=item.pk, name=item.name)
