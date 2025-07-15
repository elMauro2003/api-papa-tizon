# mensajes/serializers.py
from rest_framework import serializers
from apps.mensajes.models import Mensajes
from apps.users.api.serializers import UserSerializer 
from apps.users.models import User

class MensajeSerializer(serializers.ModelSerializer):
    remitente = UserSerializer(read_only=True)
    destinatario = UserSerializer(read_only=True)
    destinatario_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='destinatario',
        write_only=True
    )
    
    class Meta:
        model = Mensajes
        fields = '__all__'
        read_only_fields = ('remitente', 'recibido', 'created_at', 'updated_at')
        extra_kwargs = {
            'mensaje': {'required': True},
            'tipodemensaje': {'required': True},
            'img': {'required': False, 'allow_null': True},
            'tipodealerta': {'required': False, 'allow_null': True},
        }

    def create(self, validated_data):
        # Asignar automáticamente el remitente como el usuario autenticado
        validated_data['remitente'] = self.context['request'].user
        return super().create(validated_data)
    
    def to_internal_value(self, data):
        if isinstance(data, dict):
            if 'img' in data and not data['img']:
                data.pop('img')
            if 'tipodealerta' in data and not data['tipodealerta']:
                data.pop('tipodealerta')
        return super().to_internal_value(data)