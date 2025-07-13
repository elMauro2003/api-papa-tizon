# mensajes/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.mensajes.api.api import MensajeViewSet, MensajesRecibidosViewSet, MensajesEnviadosViewSet

router = DefaultRouter()
router.register(r'mensajes', MensajeViewSet, basename='mensaje')
router.register(r'mensajes-recibidos', MensajesRecibidosViewSet, basename='mensajes-recibidos')
router.register(r'mensajes-enviados', MensajesEnviadosViewSet, basename='mensajes-enviados')

urlpatterns = [
    path('api/', include(router.urls)),
]