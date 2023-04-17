from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'provider', 'create_time', 'debt']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'model', 'data']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = ('id', 'name', 'country')


class StreetSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Street
        fields = ('id', 'name', 'city')


class HouseSerializer(serializers.ModelSerializer):
    street = StreetSerializer()

    class Meta:
        model = House
        fields = ('id', 'number', 'street')


class ContactsSerializer(serializers.ModelSerializer):
    house = HouseSerializer()

    class Meta:
        model = Contacts
        fields = ('id', 'email', 'house')


class CompanyByCountrySerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(many=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'contacts')


class CompanyUpdateSerializer(CompanySerializer):
    def update(self, instance, validated_data):
        validated_data.pop('debt', None)  # remove 'debt' field from validated_data
        return super().update(instance, validated_data)