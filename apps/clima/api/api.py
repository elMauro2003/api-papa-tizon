# clima/api_views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from apps.clima.models import Clima
from apps.clima.api.serializers import ClimaSerializer
from apps.clima.api.filters import ClimaFilter
from apps.clima.utils import (
    empresas_por_estacion,
    clasificar_dia,
    severidad,
    deteccion_inicial,
    buscar_senal,
    ultima_alerta,
    tipo_diagnostico
)
from datetime import datetime, timedelta
from apps.empresa.models import Empresa

class ClimaViewSet(viewsets.ModelViewSet):
    queryset = Clima.objects.all()
    serializer_class = ClimaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClimaFilter
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'today']:
            permission_classes = [IsAuthenticated, IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        clima = serializer.save()
        
        # Lógica de procesamiento post-creación
        for emp in empresas_por_estacion(clima.estacion_id):
            clima.empresa.add(emp.id)
        
        clasificar_dia(clima.id)
        severidad(clima.id)
        deteccion_inicial(clima.id)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        clima = serializer.save()
        
        # Lógica de procesamiento post-actualización
        for emp in empresas_por_estacion(clima.estacion_id):
            clima.empresa.add(emp.id)
        
        clasificar_dia(clima.id)
        severidad(clima.id)
        deteccion_inicial(clima.id)
        
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def today(self, request):
        today_clima = Clima.objects.filter(fecha=datetime.today().strftime('%Y-%m-%d'))
        serializer = self.get_serializer(today_clima, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get', 'post'])
    def resumen_semanal(self, request):
        if request.method == 'GET':
            # Lógica para GET
            if not request.user.is_authenticated:
                return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
            
            # Verifica si el usuario tiene una empresa asociada
            if not request.user.empresa:
                return Response({'error': 'El usuario no tiene una empresa asociada'}, status=status.HTTP_400_BAD_REQUEST)
        
            defEmp = request.user.empresa.nombre
            idEmp = request.user.empresa.id
            defEnd = datetime.today()
            defStart = defEnd - timedelta(days=6)
            
            return self._calculate_weekly_summary(idEmp, defStart, defEnd, defEmp)
        
        elif request.method == 'POST':
            # Lógica para POST
            seleccion = request.data.get('empresa')
            fecha = request.data.get('fecha')
            
            if not seleccion or seleccion == 'Seleccionar una empresa':
                return Response({'error': 'Empresa no seleccionada'}, status=status.HTTP_400_BAD_REQUEST)
            
            if not fecha:
                return Response({'error': 'Fecha no seleccionada'}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                end = datetime.strptime(fecha, '%Y-%m-%d')
                start = end - timedelta(days=6)
                emp = int(seleccion)
                nomb_emp = Empresa.objects.get(id=emp).nombre
                
                return self._calculate_weekly_summary(emp, start, end, nomb_emp)
            
            except (ValueError, Empresa.DoesNotExist) as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def _calculate_weekly_summary(self, empresa_id, start_date, end_date, empresa_nombre):
        week = Clima.objects.filter(empresa=empresa_id, fecha__gte=start_date, fecha__lte=end_date)
        num_days = len(week)
        
        sev_acum = 0
        favs = 0
        det_inic = 0
        
        for day in week:
            if day.severidad is not None and day.severidad > -1:
                sev_acum += day.severidad
            if day.favorable == 1:
                favs += 1
            if day.deteccion_inicial is not None and day.deteccion_inicial > 0:
                det_inic = max(det_inic, day.deteccion_inicial)
        
        senal = buscar_senal(sev_acum, favs)
        ult_alerta = ultima_alerta(empresa_id)
        
        data = {
            'empresa': empresa_nombre,
            'dias': num_days,
            'severidad': sev_acum,
            'dias_favorables': favs,
            'deteccion': det_inic,
            'alerta': senal,
            'ult_alerta': ult_alerta.strftime('%Y-%m-%d %H:%M:%S') if ult_alerta else None,
            'start': start_date.strftime('%Y-%m-%d'),
            'end': end_date.strftime('%Y-%m-%d')
        }
        
        return Response(data)