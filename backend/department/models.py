from django.db import models

from common.models import BaseModel

class Department(BaseModel):
    department_name = models.CharField(max_length=100)
