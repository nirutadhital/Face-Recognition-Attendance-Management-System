from django.db import models

from common.models import BaseModel
from department.models import Department

class Faculty(BaseModel):
    faculty_name = models.CharField(max_length=100)
    # department=models.ForeignKey(Department, on_delete=models.CASCADE)
