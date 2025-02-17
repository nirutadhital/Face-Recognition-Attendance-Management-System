from django.shortcuts import render
from rest_framework import generics, mixins
from faculty.serializers import FacultySerializer
from faculty.models import Faculty


class FacultyListCreateAPIView(generics.ListCreateAPIView):
    queryset=Faculty.objects.all()
    serializer_class=FacultySerializer   
    
    def perform_create(self, serializer):
        serializer.save(company_id=1)

faculty_list_create_view=FacultyListCreateAPIView.as_view()


class FacultyUpdateAPIView(generics.UpdateAPIView):
    queryset=Faculty.objects.all()
    serializer_class=FacultySerializer

faculty_update_view=FacultyUpdateAPIView.as_view()



class FacultyDestroyAPIView(generics.DestroyAPIView):
    queryset=Faculty.objects.all()
    serializer_class=FacultySerializer

faculty_destroy_view=FacultyDestroyAPIView.as_view()

