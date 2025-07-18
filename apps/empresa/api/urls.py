# empresa/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.empresa.api.api import EmpresaViewSet

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet, basename='empresa')

urlpatterns = [
    path('api/', include(router.urls)),
]