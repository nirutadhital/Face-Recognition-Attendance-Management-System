from django.db import models
from common.models import BaseModel
from django.conf import settings

# from users.models import User

class Role(BaseModel):
    role_name = models.CharField(max_length=100, unique=True)
    

class UserInRole(models.Model):
    user_in_role_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'role')
