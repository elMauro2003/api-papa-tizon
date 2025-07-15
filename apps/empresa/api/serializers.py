# empresa/serializers.py
from rest_framework import serializers
from apps.empresa.models import Empresa
from apps.estacion.models import Estacion
from rest_framework.validators import UniqueValidator

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
            'nombre': {'validators': [UniqueValidator(queryset=Empresa.objects.all())]},
            'representante': {'required': True},
            'municipio': {'required': True},
            'provincia': {'required': True}
        }