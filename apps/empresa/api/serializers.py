# empresa/serializers.py
from rest_framework import serializers
from empresa.models import Empresa
from apps.estacion.models import Estacion

class EstacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacion
        fields = ['id', 'nombre']  # Ajusta según tu modelo Estacion

class EmpresaSerializer(serializers.ModelSerializer):
    estacion = EstacionSerializer(read_only=True)
    estacion_id = serializers.PrimaryKeyRelatedField(
        queryset=Estacion.objects.all(),
        source='estacion',
        write_only=True
    )
    
    class Meta:
        model = Empresa
        fields = '__all__'
        extra_kwargs = {
            'nombre': {'required': True},
            'representante': {'required': True},
            'municipio': {'required': True},
            'provincia': {'required': True}
        }