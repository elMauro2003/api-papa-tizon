# clima/serializers.py
from rest_framework import serializers
from clima.models import Clima
from apps.empresa.models import Empresa
from apps.estacion.models import Estacion

class EstacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacion
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class ClimaSerializer(serializers.ModelSerializer):
    estacion = EstacionSerializer(read_only=True)
    empresas = EmpresaSerializer(many=True, read_only=True, source='empresa')
    
    class Meta:
        model = Clima
        fields = '__all__'
        read_only_fields = ('favorable', 'severidad', 'deteccion_inicial')