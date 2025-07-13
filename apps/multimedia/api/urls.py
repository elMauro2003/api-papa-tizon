# multimedia/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.multimedia.api.api import MultimediaViewSet

router = DefaultRouter()
router.register(r'multimedia', MultimediaViewSet, basename='multimedia')

urlpatterns = [
    path('api/', include(router.urls)),
]