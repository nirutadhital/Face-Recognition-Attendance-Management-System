from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            'pk',
            'username',
            'password',
            'email',
            'photo',
            'face_embeddings',
            'added_by_id',
            'company_id',
            'department_id',
            'faculty_id',
            'grades_id',
        ]