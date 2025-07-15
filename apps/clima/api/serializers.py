# clima/serializers.py
from rest_framework import serializers
from apps.clima.models import Clima
from apps.empresa.api.serializers import EmpresaSerializer
from apps.estacion.models import Estacion
from apps.empresa.models import Empresa

class EstacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacion
        fields = '__all__'

class ClimaSerializer(serializers.ModelSerializer):
    estacion = serializers.PrimaryKeyRelatedField(queryset=Estacion.objects.all())
    empresa = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Empresa.objects.all(), required=False
    )
    
    class Meta:
        model = Clima
        fields = '__all__'
        read_only_fields = ('favorable', 'severidad', 'deteccion_inicial')