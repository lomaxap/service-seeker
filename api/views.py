from django.shortcuts import render

from models import *
from rest_framework import viewsets
from serializers import *

class OrganizationsView(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class OrganizationServicesView(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        organization_id = self.kwargs['organization_id']
        return Service.objects.filter(organization=organization_id)

class OrganizationLocationsView(viewsets.ModelViewSet):
    serializer_class = LocationSerializer

    def get_queryset(self):
        organization_id = self.kwargs['organization_id']
        return Location.objects.filter(organization=organization_id)

class OrganizationContactsView(viewsets.ModelViewSet):
    serializer_class = ContactsSerializer

    def get_queryset(self):
        organization_id = self.kwargs['organization_id']
        return Contact.objects.filter(organization=organization_id)


class ServicesView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class LocationsView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class ContactsView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializer

class HoursView(viewsets.ModelViewSet):
    queryset = Hours.objects.all()
    serializer_class = HoursSerializer

class PhonesView(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class CategoriesView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class EligibilitiesView(viewsets.ModelViewSet):
    queryset = Eligibility.objects.all()
    serializer_class = EligibilitySerializer

class TagsView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
