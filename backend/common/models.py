# from django.db import models

# class BaseModel(models.Model):
#     is_active = models.BooleanField(default=True)
#     is_deleted = models.BooleanField(default=False)
#     added_on = models.DateTimeField(auto_now_add=True)
#     added_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_added_by')
#     updated_on = models.DateTimeField(auto_now=True)
#     updated_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='%(class)s_updated_by')
#     deleted_on = models.DateTimeField(null=True, blank=True)
#     deleted_by = models.ForeignKey(
#         'User', on_delete=models.CASCADE, null=True, blank=True, related_name='%(class)s_deleted_by'
#     )

#     class Meta:
#         abstract = True

# from django.db import models
# from company.models import Company
# from users.models import User
# from django.contrib.auth import get_user_model


# User=get_user_model()
# class BaseModel(models.Model):
#     company=models.ForeignKey(Company, on_delete=models.CASCADE )
#     is_active = models.BooleanField(default=True)
#     is_deleted = models.BooleanField(default=False)
#     added_on = models.DateTimeField(auto_now_add=True)
#     added_by = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name="%(class)s_added_by")
#     updated_on = models.DateTimeField(auto_now=True, null=True)
#     updated_by = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name="%(class)s_updated_by")
#     deleted_on = models.DateTimeField(null=True, blank=True)
#     deleted_by = models.ForeignKey(
#         User, on_delete=models.CASCADE, null=True, blank=True, related_name="%(class)s_deleted_by"
#     )

#     class Meta:
#         abstract = True


from django.db import models
from company.models import Company  


class BaseModel(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)   
    added_by = models.ForeignKey('users.User', null=True, on_delete=models.CASCADE, related_name="%(class)s_added_by")
    updated_on = models.DateTimeField(auto_now=True, null=True)
    updated_by = models.ForeignKey('users.User', null=True, on_delete=models.CASCADE, related_name="%(class)s_updated_by")
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True, related_name="%(class)s_deleted_by")

    class Meta:
        abstract = True
