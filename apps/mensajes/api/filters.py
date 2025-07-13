# mensajes/filters.py
import django_filters
from apps.mensajes.models import Mensajes

class MensajeFilter1(django_filters.FilterSet):
    remitente = django_filters.CharFilter(field_name='remitente__username', lookup_expr='icontains')
    created_at = django_filters.DateFromToRangeFilter()
    tipodemensaje = django_filters.ChoiceFilter(choices=Mensajes.TMENSAJE)
    
    class Meta:
        model = Mensajes
        fields = ['remitente', 'tipodemensaje', 'created_at']

class MensajeFilter2(django_filters.FilterSet):
    destinatario = django_filters.CharFilter(field_name='destinatario__username', lookup_expr='icontains')
    created_at = django_filters.DateFromToRangeFilter()
    tipodemensaje = django_filters.ChoiceFilter(choices=Mensajes.TMENSAJE)
    
    class Meta:
        model = Mensajes
        fields = ['destinatario', 'tipodemensaje', 'created_at']