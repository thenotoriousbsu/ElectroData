from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)
    provider = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, default=None)
    create_time = models.DateTimeField('time of creation', auto_now_add=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=100, blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    first_name = models.CharField(max_length=100, default='Vasya')
    last_name = models.CharField(max_length=100, default='Pupkin')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=12)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    data = models.DateTimeField('product launch date')
    company = models.ManyToManyField(Company, blank=True, related_name='product', through='Gap')

    def __str__(self):
        return f'{self.name}-{self.model}'


class Gap(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['product', 'company']]


class Country(models.Model):
    country = models.CharField(max_length=50, default='Belarus')

    def __str__(self):
        return f'{self.country}'


class City(models.Model):
    city = models.CharField(max_length=50, default='Minsk')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.city}'


class Street(models.Model):
    street = models.CharField(max_length=50, default='Lenina')
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.street}'


class House(models.Model):
    house_number = models.CharField(max_length=20, default=1)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.house_number}'


class Contacts(models.Model):
    email = models.EmailField("email address", blank=True)
    house = models.OneToOneField(House, on_delete=models.CASCADE, default=1, primary_key=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.company_id} - {self.email}'
