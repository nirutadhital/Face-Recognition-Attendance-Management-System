from django.db import models

from common.models import BaseModel

class Holiday(BaseModel):
    holiday_name = models.CharField(max_length=100)