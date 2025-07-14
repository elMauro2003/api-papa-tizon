# extras/serializers.py
from rest_framework import serializers
from apps.extras.models import Aparicion, DatosPlantacion
from apps.empresa.api.serializers import EmpresaSerializer
from apps.empresa.models import Empresa

class AparicionSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(read_only=True)
    empresa_id = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(),
        source='empresa',
        write_only=True
    )
    
    class Meta:
        model = Aparicion
        fields = '__all__'
        read_only_fields = ('fecha',)

class DatosPlantacionSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer(read_only=True)
    empresa_id = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(),
        source='empresa',
        write_only=True
    )
    
    class Meta:
        model = DatosPlantacion
        fields = '__all__'
        extra_kwargs = {
            'cultivar': {'required': True},
            'fecha': {'required': True},
            'porcentaje': {'required': True}
        }