from django.db import models

from common.models import BaseModel
from users.models import User

    
class Leave(BaseModel):
    leave_name=models.CharField(max_length=100)
    
    
class UserInLeave(BaseModel):
    user_in_leave_id=models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave = models.ForeignKey(Leave, on_delete=models.CASCADE)
    description=models.CharField(max_length=100)
