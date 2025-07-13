# empresa/serializers.py
from rest_framework import serializers
from apps.empresa.models import Empresa
from apps.estacion.models import Estacion

class EmpresaSerializer(serializers.ModelSerializer):
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