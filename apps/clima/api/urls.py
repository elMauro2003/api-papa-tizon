# clima/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.clima.api_views import ClimaViewSet

router = DefaultRouter()
router.register(r'clima', ClimaViewSet, basename='clima')

urlpatterns = [
    path('api/', include(router.urls)),
    # Mantener las URLs originales para compatibilidad si es necesario
    path('lista_clima', ClimaList.as_view(), name="lista_clima"),
    path('lista_clima_hoy', ClimaListToday.as_view(), name="lista_clima_hoy"),
    path('crear_clima', ClimaCreate.as_view(), name="crear_clima"),
    path('editar_clima/<pk>/', ClimaUpdate.as_view(), name="editar_clima"),
    path('resumen_semanal', ResumenSemanal.as_view(), name="resumen_semanal")
]