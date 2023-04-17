from django.contrib import admin
from .models import *
from django.db.models import QuerySet


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time', 'provider', 'debt']
    list_display_links = ['name', 'provider']
    list_editable = ['debt']
    actions = ['debt_clearance']
    list_filter = ["contacts__house__street__city"]

    @admin.action(description="Сlean up debt from dedicated companies")
    def debt_clearance(self, request, queryset):
        count_updated = queryset.update(debt=0)
        self.message_user(
            request,
            f'Задолженность очищена у {count_updated} компаний'
        )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'company']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'data']


@admin.register(Gap)
class GapAdmin(admin.ModelAdmin):
    list_display = ['company_id', 'product_id']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['country']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['city', 'country']


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ['street', 'city']


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'house_number', 'street']


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['company', 'email', 'house']