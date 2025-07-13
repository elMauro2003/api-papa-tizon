# empresa/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.empresa.api.api import EmpresaViewSet
from empresa.views import EmpresaCreate, EmpresaList, EmpresaDelete, EmpresaUpdate

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet, basename='empresa')

api_urlpatterns = [
    path('api/', include(router.urls)),
]

# Mantener las URLs originales para compatibilidad
web_urlpatterns = [
    path('lista_empresas', EmpresaList.as_view(), name="lista_empresa"),
    path('crear_empresa', EmpresaCreate.as_view(), name="crear_empresa"),
    path('eliminar_empresa/<pk>/', EmpresaDelete.as_view(), name="eliminar_empresa"),
    path('editar_empresa/<pk>/', EmpresaUpdate.as_view(), name="editar_empresa"),
]

urlpatterns = api_urlpatterns + web_urlpatterns