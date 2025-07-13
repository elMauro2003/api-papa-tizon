# clima/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.clima.api.api import ClimaViewSet

router = DefaultRouter()
router.register(r'clima', ClimaViewSet, basename='clima')

urlpatterns = [
    path('api/', include(router.urls))
]