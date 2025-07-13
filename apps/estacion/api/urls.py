# estacion/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.estacion.api.api import EstacionViewSet

router = DefaultRouter()
router.register(r'estaciones', EstacionViewSet, basename='estacion')

urlpatterns = [
    path('api/', include(router.urls)),
]
