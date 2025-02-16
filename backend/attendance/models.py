from django.db import models
from common.models import BaseModel
from users.models import User

class Attendance(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
