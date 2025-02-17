from django.shortcuts import render
from rest_framework import generics, mixins
from leave.serializers import LeaveSerializer
from leave.models import Leave


class LeaveListCreateAPIView(generics.ListCreateAPIView):
    queryset=Leave.objects.all()
    serializer_class=LeaveSerializer   
    
    def perform_create(self, serializer):
        serializer.save(company_id=1)

leave_list_create_view=LeaveListCreateAPIView.as_view()


class LeaveUpdateAPIView(generics.UpdateAPIView):
    queryset=Leave.objects.all()
    serializer_class=LeaveSerializer

leave_update_view=LeaveUpdateAPIView.as_view()



class LeaveDestroyAPIView(generics.DestroyAPIView):
    queryset=Leave.objects.all()
    serializer_class=LeaveSerializer

leave_destroy_view=LeaveDestroyAPIView.as_view()
