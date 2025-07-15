# users/api_views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserApprovalSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve', 'logout']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        return User.objects.all() if user.is_admin else User.objects.filter(id=user.id)

    @action(detail=False, methods=['get'])
    def pending_approval(self, request):
        if not request.user.is_admin:
            return Response(
                {'error': 'No tienes permisos para realizar esta acción'},
                status=status.HTTP_403_FORBIDDEN
            )
        pending_users = User.objects.filter(aprobado=False)
        serializer = self.get_serializer(pending_users, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        if not request.user.is_admin:
            return Response(
                {'error': 'No tienes permisos para realizar esta acción'},
                status=status.HTTP_403_FORBIDDEN
            )
        user.aprobado = True
        user.save()
        serializer = UserApprovalSerializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        logout(request)
        return Response({'message': 'Sesión cerrada correctamente'})