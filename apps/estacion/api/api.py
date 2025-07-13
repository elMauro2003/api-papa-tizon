# estacion/api_views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from apps.estacion.models import Estacion
from apps.estacion.api.serializers import EstacionSerializer

class EstacionViewSet(viewsets.ModelViewSet):
    queryset = Estacion.objects.all()
    serializer_class = EstacionSerializer
    lookup_field = 'num_estacion'
    
    def get_permissions(self):
        """
        Los usuarios normales solo pueden listar y ver estaciones
        Los admin pueden hacer todas las operaciones
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Verificar si la estación ya existe
        if Estacion.objects.filter(num_estacion=serializer.validated_data['num_estacion']).exists():
            return Response(
                {'error': 'Ya existe una estación con este número'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        # Verificar si se está cambiando el num_estacion y si ya existe
        if 'num_estacion' in serializer.validated_data:
            new_num = serializer.validated_data['num_estacion']
            if new_num != instance.num_estacion and Estacion.objects.filter(num_estacion=new_num).exists():
                return Response(
                    {'error': 'Ya existe una estación con este número'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        self.perform_update(serializer)
        return Response(serializer.data)