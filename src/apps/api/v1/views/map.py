from rest_framework import generics

from apps.api.auth.csrf_exempt import CsrfExemptSessionAuthentication
from apps.api.v1.serializers.map import CreateRequestMapSerializer


class CreateMapRequestView(generics.CreateAPIView):
    serializer_class = CreateRequestMapSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, )
