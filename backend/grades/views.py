from django.shortcuts import render
from rest_framework import generics, mixins
from grades.serializers import GradesSerializer
from grades.models import Grades


class GradesListCreateAPIView(generics.ListCreateAPIView):
    queryset=Grades.objects.all()
    serializer_class=GradesSerializer   
    
    def perform_create(self, serializer):
        serializer.save(company_id=1)

grades_list_create_view=GradesListCreateAPIView.as_view()


class GradesUpdateAPIView(generics.UpdateAPIView):
    queryset=Grades.objects.all()
    serializer_class=GradesSerializer

grades_update_view=GradesUpdateAPIView.as_view()



class GradesDestroyAPIView(generics.DestroyAPIView):
    queryset=Grades.objects.all()
    serializer_class=GradesSerializer

grades_destroy_view=GradesDestroyAPIView.as_view()

