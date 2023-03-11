from django.contrib.auth.models import User

from apps.maps.factory.map import MapFactory
from apps.maps.models.map import Map


class MapRepository:

    def __init__(self):
        self.model = Map
        self.user_model = User
        self.factory = MapFactory()

    def create(self, user_email):
        user = User.objects.get(email=user_email)
        map = self.model.objects.create(user=user)
        return self.factory.dto_from_model(map)
