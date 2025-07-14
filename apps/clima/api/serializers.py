# clima/serializers.py
from rest_framework import serializers
from apps.clima.models import Clima
from apps.empresa.api.serializers import EmpresaSerializer
from apps.estacion.models import Estacion

class EstacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacion
        fields = '__all__'

class ClimaSerializer(serializers.ModelSerializer):
    #estacion = EstacionSerializer(read_only=True)
    estacion = serializers.PrimaryKeyRelatedField(queryset=Estacion.objects.all())
    empresas = EmpresaSerializer(many=True, read_only=True, source='empresa')
    
    class Meta:
        model = Clima
        fields = '__all__'
        read_only_fields = ('favorable', 'severidad', 'deteccion_inicial')