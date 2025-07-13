# mensajes/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.mensajes.api.api import MensajeViewSet, MensajesRecibidosViewSet, MensajesEnviadosViewSet
from mensajes.views import MensajeCreate, MensajeDetalle, RecibidosListView, EnviadosListView

router = DefaultRouter()
router.register(r'mensajes', MensajeViewSet, basename='mensaje')
router.register(r'mensajes-recibidos', MensajesRecibidosViewSet, basename='mensajes-recibidos')
router.register(r'mensajes-enviados', MensajesEnviadosViewSet, basename='mensajes-enviados')

api_urlpatterns = [
    path('api/', include(router.urls)),
]

# Mantener las URLs originales para compatibilidad
web_urlpatterns = [
    path('mensajes_recibidos', RecibidosListView.as_view(), name="mensajes_recibidos"),
    path('mensajes_enviados', EnviadosListView.as_view(), name="mensajes_enviados"),
    path('mensaje_detalle/<pk>/', MensajeDetalle.as_view(), name="mensaje_detalle"),
    path('redactar_mensaje', MensajeCreate.as_view(), name="redactar_mensaje"),
]

urlpatterns = api_urlpatterns + web_urlpatterns