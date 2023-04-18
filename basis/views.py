from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg
from .models import *
from .serializers import *
from .permissions import *


class CompanyListView(ListAPIView):
    permission_classes = [IsActiveUser]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyListByCountry(generics.ListAPIView):
    permission_classes = [IsActiveUser]
    serializer_class = CompanySerializer

    def get_queryset(self):
        country = self.kwargs['country_name']
        return Company.objects.filter(contacts__house__street__city__country__country=country)


class DebtAboveAVGCompaniesView(generics.ListAPIView):
    permission_classes = [IsActiveUser]
    serializer_class = CompanySerializer

    def get_queryset(self):
        avg_debt = Company.objects.aggregate(Avg('debt'))['debt__avg']
        queryset = Company.objects.filter(debt__gt=avg_debt)

        return queryset


class ProductByCompanyView(generics.ListAPIView):
    permission_classes = [IsActiveUser]
    serializer_class = CompanySerializer

    def get_queryset(self):
        product = self.kwargs['id']
        return Company.objects.filter(gap__product_id=product)


class CompanyCreateView(CreateAPIView):
    permission_classes = [IsActiveUser]
    serializer_class = CompanySerializer


class CompanyUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsActiveUser]
    queryset = Company.objects.all()
    serializer_class = CompanyUpdateSerializer


class CompanyDeleteView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsActiveUser]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
