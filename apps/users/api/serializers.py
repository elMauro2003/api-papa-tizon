# users/serializers.py
from rest_framework import serializers
from apps.users.models import User
from apps.empresa.models import Empresa
from apps.empresa.api.serializers import EmpresaSerializer

class UserSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(read_only=True)
    empresa_id = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(),
        source='empresa',
        write_only=True,
        required=True
    )
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'password', 'first_name', 'last_name',
            'empresa', 'empresa_id', 'cargo', 'edad', 'sexo', 
            'is_admin', 'is_normal', 'aprobado'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'is_admin': {'read_only': True},
            'is_normal': {'read_only': True},
            'aprobado': {'read_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            empresa=validated_data['empresa'],
            cargo=validated_data['cargo'],
            edad=validated_data['edad'],
            sexo=validated_data['sexo'],
            is_normal=True  # Todos los nuevos usuarios son normales por defecto
        )
        return user

class UserApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'aprobado']
        read_only_fields = ['id', 'username']