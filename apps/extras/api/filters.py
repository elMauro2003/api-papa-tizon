# extras/filters.py
import django_filters
from extras.models import Aparicion, DatosPlantacion

class CultivarFilter(django_filters.FilterSet):
    empresa = django_filters.CharFilter(field_name='empresa__nombre', lookup_expr='icontains')
    fecha = django_filters.DateFromToRangeFilter()
    
    class Meta:
        model = Aparicion
        fields = ['empresa', 'fecha']

class DatosPlantacionFilter(django_filters.FilterSet):
    empresa = django_filters.CharFilter(field_name='empresa__nombre', lookup_expr='icontains')
    cultivar = django_filters.CharFilter(lookup_expr='icontains')
    fecha = django_filters.DateFromToRangeFilter()
    
    class Meta:
        model = DatosPlantacion
        fields = ['empresa', 'cultivar', 'fecha', 'porcentaje']