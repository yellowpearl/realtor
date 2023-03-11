from django.urls import path

from apps.api.v1.views.map import CreateMapRequestView

urlpatterns = [
    path("create_map", CreateMapRequestView.as_view()),
]