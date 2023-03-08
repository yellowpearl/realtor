from django.contrib import admin

from apps.maps.models import Map, Choice, TransportType, TravelTime

admin.site.register(Map)
admin.site.register(Choice)
admin.site.register(TransportType)
admin.site.register(TravelTime)