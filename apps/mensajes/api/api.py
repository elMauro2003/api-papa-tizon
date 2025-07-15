# mensajes/api_views.py
from rest_framework import viewsets, filters
from apps.mensajes.models import Mensajes
from apps.mensajes.api.serializers import MensajeSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from apps.mensajes.api.filters import MensajeFilter1, MensajeFilter2
from django.db.models import Q

class MensajeViewSet(viewsets.ModelViewSet):
    serializer_class = MensajeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['created_at']
    
    def get_queryset(self):
        # Filtra mensajes donde el usuario es remitente o destinatario
        return Mensajes.objects.filter(
            Q(destinatario=self.request.user) | Q(remitente=self.request.user)
        ).select_related('remitente', 'destinatario').distinct()

    def perform_create(self, serializer):
        # Marcar automáticamente el mensaje como no recibido al crearlo
        serializer.save(recibido=False)

class MensajesRecibidosViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MensajeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MensajeFilter1
    
    def get_queryset(self):
        return Mensajes.objects.filter(destinatario=self.request.user)

class MensajesEnviadosViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MensajeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MensajeFilter2
    
    def get_queryset(self):
        return Mensajes.objects.filter(remitente=self.request.user)