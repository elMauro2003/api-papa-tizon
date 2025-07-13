# empresa/api_views.py
from rest_framework import viewsets, permissions
from apps.empresa.models import Empresa
from apps.empresa.api.serializers import EmpresaSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    
    def get_permissions(self):
        """
        Instancia y retorna la lista de permisos que requiere esta vista.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]