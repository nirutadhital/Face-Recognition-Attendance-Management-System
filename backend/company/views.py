from django.shortcuts import render
from rest_framework import generics, mixins
from company.serializers import CompanySerializer
from company.models import Company



class CompanyListCreateAPIView(generics.ListCreateAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

company_list_create_view=CompanyListCreateAPIView.as_view()


class CompanyUpdateAPIView(generics.UpdateAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

company_update_view=CompanyUpdateAPIView.as_view()



class CompanyDestroyAPIView(generics.DestroyAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

company_destroy_view=CompanyDestroyAPIView.as_view()