# extras/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.extras.api.api import AparicionViewSet, DatosPlantacionViewSet

router = DefaultRouter()
router.register(r'apariciones', AparicionViewSet, basename='aparicion')
router.register(r'datos-plantacion', DatosPlantacionViewSet, basename='datos-plantacion')

urlpatterns = [
    path('api/', include(router.urls)),
]