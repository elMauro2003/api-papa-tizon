# clima/filters.py
import django_filters
from apps.clima.models import Clima

class ClimaFilter(django_filters.FilterSet):
    estacion = django_filters.CharFilter(field_name='estacion__nombre', lookup_expr='icontains')
    fecha = django_filters.DateFromToRangeFilter()
    temperatura_media = django_filters.RangeFilter()
    temperatura_maxima = django_filters.RangeFilter()
    temperatura_minima = django_filters.RangeFilter()
    precipitacion = django_filters.RangeFilter()
    favorable = django_filters.NumberFilter()
    severidad = django_filters.NumberFilter()
    deteccion_inicial = django_filters.NumberFilter()

    class Meta:
        model = Clima
        fields = [
            'estacion', 
            'fecha', 
            'temperatura_media', 
            'temperatura_maxima', 
            'temperatura_minima', 
            'precipitacion', 
            'favorable', 
            'severidad', 
            'deteccion_inicial'
        ]