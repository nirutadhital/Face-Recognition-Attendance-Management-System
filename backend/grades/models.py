from django.db import models

from common.models import BaseModel
from faculty.models import Faculty

class Grades(BaseModel):
    grade_name = models.CharField(max_length=100)
    # faculty=models.ForeignKey(Faculty, on_delete=models.CASCADE)
