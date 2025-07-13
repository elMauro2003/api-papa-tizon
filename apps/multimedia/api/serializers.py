# multimedia/serializers.py
from rest_framework import serializers
from apps.empresa.models import Empresa
from datetime import datetime

class GraphicDataSerializer(serializers.Serializer):
    empresa = serializers.PrimaryKeyRelatedField(queryset=Empresa.objects.all())
    fecha_inicio = serializers.DateField()
    fecha_fin = serializers.DateField()

    def validate(self, data):
        if data['fecha_inicio'] > data['fecha_fin']:
            raise serializers.ValidationError("La fecha de inicio debe ser anterior a la fecha final")
        return data