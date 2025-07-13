# estacion/serializers.py
from rest_framework import serializers
from estacion.models import Estacion

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

    def validate_num_estacion(self, value):
        """
        Validación personalizada para el número de estación
        """
        if len(value) != 6:
            raise serializers.ValidationError("El número de estación debe tener exactamente 6 caracteres")
        return value