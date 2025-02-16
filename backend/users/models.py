from django.db import models
from department.models import Department
from faculty.models import Faculty
from grades.models import Grades
from common.models import BaseModel


class User(BaseModel):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128, null=False)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='photos/')
    face_embeddings = models.TextField(blank=True, null=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    grades=models.ForeignKey(Grades,on_delete=models.CASCADE)
    



    
    
    
    
