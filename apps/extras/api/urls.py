# extras/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.extras.api.api import AparicionViewSet, DatosPlantacionViewSet
from extras.views import (AparicionView, PorcentajeCreateView, PorcentajeListView, 
                         AparicionListView, AparicionDelete, PorcentajeDelete)

router = DefaultRouter()
router.register(r'apariciones', AparicionViewSet, basename='aparicion')
router.register(r'datos-plantacion', DatosPlantacionViewSet, basename='datos-plantacion')

api_urlpatterns = [
    path('api/', include(router.urls)),
]

# Mantener las URLs originales para compatibilidad
web_urlpatterns = [
    path('aparicion', AparicionView.as_view(), name="aparicion"),
    path('aparicion_delete/<pk>/', AparicionDelete.as_view(), name="aparicion_delete"),
    path('aparicion_list', AparicionListView.as_view(), name="aparicion_list"),
    path('porcentaje', PorcentajeCreateView.as_view(), name="porcentaje"),
    path('porcentaje_delete/<pk>/', PorcentajeDelete.as_view(), name="porcentaje_delete"),
    path('porcentaje_list', PorcentajeListView.as_view(), name="porcentaje_list"),
]

urlpatterns = api_urlpatterns + web_urlpatterns