# multimedia/api_views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.multimedia.api.serializers import GraphicDataSerializer
from apps.multimedia.utils import contextGraph, set_fechas
from empresa.models import Empresa
from django.http import FileResponse
import os
from pathlib import Path

class MultimediaViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def generate_graphic_data(self, request):
        serializer = GraphicDataSerializer(data=request.data)
        if serializer.is_valid():
            data = contextGraph(serializer.validated_data)
            if not data:
                return Response(
                    {'error': 'No hay datos para el rango de fechas seleccionado'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def default_graphic_data(self, request):
        default_emp = request.user.empresa.id
        start, end = set_fechas()
        data = {
            'empresa': default_emp,
            'fecha_inicio': start.strftime('%Y-%m-%d'),
            'fecha_fin': end.strftime('%Y-%m-%d')
        }
        graphic_data = contextGraph({
            'empresa': default_emp,
            'fecha_inicio': start,
            'fecha_fin': end
        })
        return Response({
            'form_data': data,
            'graphic_data': graphic_data
        })

    @action(detail=False, methods=['get'])
    def download_manual(self, request):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = "ManualUsuario.pdf"
        filepath = os.path.join(BASE_DIR, 'static', 'vendor', filename)
        
        if os.path.exists(filepath):
            return FileResponse(open(filepath, 'rb'), as_attachment=True, filename=filename)
        return Response(
            {'error': 'El archivo no existe'},
            status=status.HTTP_404_NOT_FOUND
        )