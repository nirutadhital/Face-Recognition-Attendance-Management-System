from django.contrib.auth.models import AbstractUser
import binascii
from datetime import timezone
import os
from django.db import models
from department.models import Department
from faculty.models import Faculty
from grades.models import Grades
from company.models import Company
from common.models import BaseModel


class User(AbstractUser):
    photo = models.ImageField(upload_to='photos/')
    face_embeddings = models.TextField(blank=True, null=True)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    grades=models.ForeignKey(Grades,on_delete=models.CASCADE)

      

'''
    1. A token is generated at the time of signup and login and store in db and returned to the client
    2. The client place the token in the Authorization header for every request
    3. For every request the server validate the token, fetches the associated user details and check if the user has access to the requested endpoint
    4. based on ther users role or permission, the server allows or denies access to the endpoint
    5. For every logout of the user, delete the token from the database
'''
class Token(models.Model):
    key=models.CharField("key",max_length=40, primary_key=True)
    user=models.ForeignKey('users.User', related_name="user_auth_token",on_delete=models.CASCADE, verbose_name=("User"))
    addedOn=models.DateTimeField(auto_now_add=True)
    
    # class  Meta:
    #     unique_together=["user","token"]
    
    def save(self, *args, **kwargs):
        if not self.key:
            self.key=self.generate_key()
        
        token=super().save(*args, **kwargs)
        
        # self.user.last_login=timezone.now()
        self.user.save()
        return token
    
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()
    
    def __str__(self):
        return self.key
        
    



    
    
    
    
