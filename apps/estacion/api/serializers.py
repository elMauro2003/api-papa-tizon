# estacion/serializers.py
from rest_framework import serializers
from apps.estacion.models import Estacion

class EstacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacion
        fields = '__all__'
        extra_kwargs = {
            'num_estacion': {
                'required': True,
                'validators': []  # Removemos validadores únicos para manejo personalizado
            },
            'nombre': {'required': True},
            'provincia': {'required': True}
        }
