import datetime
from django.utils import timezone
from rest_framework import serializers
from .models import *

# from djoser.serializers import UserCreateSerializer
# from rest_framework_jwt.settings import api_settings
# from django.contrib.auth import get_user_model


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'provider', 'create_time', 'debt', 'user']


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
    name = serializers.CharField(max_length=50, required=True)

    def update(self, instance, validated_data):
        validated_data.pop('debt', None)
        return super().update(instance, validated_data)


class ProductUpdateSerializer(ProductSerializer):
    name = serializers.CharField(max_length=25, required=True)

    def validate_data(self, data):
        if data > timezone.now():
            raise serializers.ValidationError("The date cannot be in the future!")
        return data

#
# User = get_user_model()
#
# class CustomUserCreateSerializer(UserCreateSerializer):
#     def create(self, validated_data):
#         user = super().create(validated_data)
#         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#         jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#         payload = jwt_payload_handler(user)
#         user.token = jwt_encode_handler(payload)
#         user.save()
#         return user
#
#     class Meta(UserCreateSerializer.Meta):
#         model = User
#         fields = ('id', 'email', 'password', 'first_name', 'last_name')