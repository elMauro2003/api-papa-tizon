# empresa/filters.py
import django_filters
from empresa.models import Empresa

class EmpresaFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    municipio = django_filters.CharFilter(lookup_expr='icontains')
    provincia = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Empresa
        fields = ['nombre', 'municipio', 'provincia', 'estacion']