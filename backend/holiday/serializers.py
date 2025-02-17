from rest_framework import serializers
from holiday.models import Holiday


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model=Holiday
        fields=[
            'pk',
            'holiday_name',
        ]