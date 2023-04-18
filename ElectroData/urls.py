"""
URL configuration for ElectroData project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from basis.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies/', CompanyListView.as_view(), name='company-list'),
    #path('companies/', UserCompanyListView.as_view(), name='company-by-user-list'),
    path('companies/create/', CompanyCreateView.as_view(), name='company-create'),
    path('companies/country/<str:country_name>/', CompanyListByCountry.as_view(), name='company-list-by-country'),
    path('companies/above_avg/', DebtAboveAVGCompaniesView.as_view(), name='above-avg-companies'),
    path('company/with/products/<str:id>/', ProductByCompanyView.as_view(), name='company-by-product'),
    path('companies/update/<int:pk>/', CompanyUpdateView.as_view(), name='company-update'),
    path('companies/product_update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('companies/delete/<int:pk>/', CompanyDeleteView.as_view(), name='company-delete'),
]
