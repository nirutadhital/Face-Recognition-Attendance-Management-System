from rest_framework import serializers
from company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=[
            'pk',
            'company_name',
            'address',
            'contact',
            'email',
            'print_logo',
            'application_logo',
            'terms_and_conditions',
            'company_vat_no',
            'company_pan_no',
        ]