from rest_framework import viewsets
from .models import User, Role, UserProjectRole
from .serializers import UserSerializer, RoleSerializer, UserProjectRoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserProjectRoleViewSet(viewsets.ModelViewSet):
    queryset = UserProjectRole.objects.all()
    serializer_class = UserProjectRoleSerializer
