from django.contrib import admin

from apps.maps.models.choice import Choice
from apps.maps.models.map import Map
from apps.maps.models.place import Place
from apps.maps.models.transport import TransportType
from apps.maps.models.travel_time import TravelTime


admin.site.register(Map)
admin.site.register(Choice)
admin.site.register(TransportType)
admin.site.register(TravelTime)
admin.site.register(Place)
