from rest_framework import serializers
from users.models import User
from django.contrib.auth.hashers import make_password


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
            'company_id',
            'department_id',
            'faculty_id',
            'grades_id',
        ]
        extra_kwargs={'password':{'write_only':True}}
        
    def create(self, validate_data):     
        user=User.objects.create_user(#Password hashing is handled by Django create_user method in the userSerialiser,,no need to manually hash it 
            username=validate_data['username'],
            password=validate_data['password'],
            email=validate_data['email'],
            photo=validate_data['photo'],
            company_id=validate_data['company_id'],  
            department_id=validate_data['department_id'],  
            faculty_id=validate_data['faculty_id'],  
            grades_id=validate_data['grades_id'],  
      
        )
            
        return user
            