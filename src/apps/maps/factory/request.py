from apps.maps.dto.request import RequestMapDto, RequestChoiceDto


class RequestChoiceFactory:

    def __init__(self):
        self.dto = RequestChoiceDto

    def dto_from_dict(self, data: dict) -> RequestChoiceDto:
        return self.dto(
            transport=data["transport"],
            travel_time=data["travel_time"],
            place=data["place"]
        )


class RequestMapFactory:

    def __init__(self):
        self.request_choice_factory = RequestChoiceFactory()
        self.dto = RequestMapDto

    def dto_from_dict(self, data: dict) -> RequestMapDto:
        return self.dto(
            choices=[self.request_choice_factory.dto_from_dict(choice) for choice in data["choices"]],
            email=data["email"],
            is_paid=data["is_paid"]
        )