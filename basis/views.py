from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg
from .models import *
from .serializers import *


class CompanyListView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyListByCountry(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        country = self.kwargs['country_name']
        return Company.objects.filter(contacts__house__street__city__country__country=country)


class DebtAboveAVGCompaniesView(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        avg_debt = Company.objects.aggregate(Avg('debt'))['debt__avg']
        queryset = Company.objects.filter(debt__gt=avg_debt)

        return queryset


class ProductByCompanyView(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        product = self.kwargs['id']
        return Company.objects.filter(gap__product_id=product)


class CompanyCreateView(CreateAPIView):
    serializer_class = CompanySerializer


class CompanyUpdateView(UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyUpdateSerializer


class CompanyDeleteView(DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
