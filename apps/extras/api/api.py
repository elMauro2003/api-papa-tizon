# extras/api_views.py
from rest_framework import viewsets
from extras.models import Aparicion, DatosPlantacion
from apps.extras.api.serializers import AparicionSerializer, DatosPlantacionSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from apps.extras.api.filters import CultivarFilter

class AparicionViewSet(viewsets.ModelViewSet):
    queryset = Aparicion.objects.all()
    serializer_class = AparicionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CultivarFilter
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]

class DatosPlantacionViewSet(viewsets.ModelViewSet):
    queryset = DatosPlantacion.objects.all()
    serializer_class = DatosPlantacionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CultivarFilter
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]