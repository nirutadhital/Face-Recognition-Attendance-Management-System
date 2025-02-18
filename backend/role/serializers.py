from rest_framework import serializers
from role.models import Role, UserInRole


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields=[
            'pk',
            'role_name',
        ]
        
class UserInRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserInRole
        fields=[
            'pk',
            'user',
            'role',      
        ]