# users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.users.api.api import UserViewSet
from apps.users.views import index, RegistroUsuario, UserList, UserDelete, UserAprove
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

api_urlpatterns = [
    path('api/', include(router.urls)),
]

# Mantener las URLs originales para compatibilidad
web_urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name="registrar"),
    path('logout', logout_then_login, name="logout"),
    path('listado_usuario', UserList.as_view(), name="lista_users"),
    path('eliminar_usuario/<pk>/', UserDelete.as_view(), name="eliminar_user"),
    path('aprobar_usuario/<pk>/', UserAprove.as_view(), name="aprobar_user"),
]

urlpatterns = api_urlpatterns + web_urlpatterns