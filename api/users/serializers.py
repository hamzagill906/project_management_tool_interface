from rest_framework import serializers
from .models import User, Role, UserProjectRole

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserProjectRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProjectRole
        fields = '__all__'
