from models import *
from rest_framework import serializers


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization

class ServiceSerializer(serializers.ModelSerializer):
    eligibilities = serializers.StringRelatedField(many=True)
    class Meta:
        model = Service

class LocationSerializer(serializers.ModelSerializer):
    services = serializers.StringRelatedField(many=True)
    class Meta:
        model = Location

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact

class HoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hours

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

class EligibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Eligibility

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
