# multimedia/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.multimedia.api.api import MultimediaViewSet
from multimedia.views import downloadManual, dataGraphic

router = DefaultRouter()
router.register(r'multimedia', MultimediaViewSet, basename='multimedia')

api_urlpatterns = [
    path('api/', include(router.urls)),
]

# Mantener las URLs originales para compatibilidad
web_urlpatterns = [
    path('downloadManual', downloadManual, name="downloadManual"),
    path('graficos', dataGraphic, name="graficos"),
]

urlpatterns = api_urlpatterns + web_urlpatterns