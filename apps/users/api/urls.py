# users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.users.api.api import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('api/', include(router.urls)),
]