from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    print_logo = models.CharField(max_length=100)
    application_logo = models.CharField(max_length=100)
    terms_and_conditions = models.CharField(max_length=100)
    company_vat_no = models.CharField(max_length=100)
    company_pan_no = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey('users.User', null=True, on_delete=models.CASCADE, related_name="%(class)s_added_by")
    updated_on = models.DateTimeField(auto_now=True, null=True)
    updated_by = models.ForeignKey('users.User', null=True, on_delete=models.CASCADE, related_name="%(class)s_updated_by")
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True, related_name="%(class)s_deleted_by")

