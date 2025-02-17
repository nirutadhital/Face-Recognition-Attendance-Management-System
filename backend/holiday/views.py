from django.shortcuts import render
from rest_framework import generics, mixins
from holiday.serializers import HolidaySerializer
from holiday.models import Holiday


class HolidayListCreateAPIView(generics.ListCreateAPIView):
    queryset=Holiday.objects.all()
    serializer_class=HolidaySerializer   
    
    def perform_create(self, serializer):
        serializer.save(company_id=1)

holiday_list_create_view=HolidayListCreateAPIView.as_view()


class HolidayUpdateAPIView(generics.UpdateAPIView):
    queryset=Holiday.objects.all()
    serializer_class=HolidaySerializer

holiday_update_view=HolidayUpdateAPIView.as_view()



class HolidayDestroyAPIView(generics.DestroyAPIView):
    queryset=Holiday.objects.all()
    serializer_class=HolidaySerializer

holiday_destroy_view=HolidayDestroyAPIView.as_view()


