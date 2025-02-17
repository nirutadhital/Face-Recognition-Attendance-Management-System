from rest_framework import serializers
from grades.models import Grades


class GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Grades
        fields=[
            'pk',
            'grade_name',
        ]