# mensajes/serializers.py
from rest_framework import serializers
from apps.mensajes.models import Mensajes
from apps.users.api.serializers import UserSerializer  # Asume que tienes un serializer para User
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
            'img': {'required': False}
        }

    def create(self, validated_data):
        # Asignar automáticamente el remitente como el usuario autenticado
        validated_data['remitente'] = self.context['request'].user
        return super().create(validated_data)
    
    def to_internal_value(self, data):
        # Manejar correctamente los datos multipart (para imágenes)
        if isinstance(data, dict) and 'img' in data and isinstance(data['img'], str):
            if not data['img']:
                data.pop('img')
        return super().to_internal_value(data)