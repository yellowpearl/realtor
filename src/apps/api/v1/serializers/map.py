from rest_framework import serializers

from apps.maps.service.map import MapService


class ChoiceSerializer(serializers.Serializer):
    transport = serializers.CharField()
    travel_time = serializers.IntegerField()
    place = serializers.CharField()


class CreateRequestMapSerializer(serializers.Serializer):
    choices = ChoiceSerializer(many=True)
    email = serializers.EmailField()
    is_paid = serializers.BooleanField()

    def create(self, validated_data):
        return MapService().create_from_data(validated_data)
