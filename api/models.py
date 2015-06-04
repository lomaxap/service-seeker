from django.db import models
from datetime import datetime

class Organization(models.Model):
    name = models.CharField('Name', max_length=255)
    description = models.TextField('Description', blank=True)
    email = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)

    parent_organization = models.ForeignKey('self', verbose_name='Parent Organization', null=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class Service(models.Model):
    organization = models.ForeignKey('Organization', verbose_name='Organization', related_name='services')
    category = models.ForeignKey('Category', verbose_name='Category', related_name='services')
    tags = models.ManyToManyField('Tag', verbose_name='Tags', related_name='services')
    locations = models.ManyToManyField('Location', verbose_name='Locations', related_name='services')

    name = models.CharField('Name', max_length=255)
    description = models.TextField('Description', blank=True)
    application_process = models.TextField('Appication Process', blank=True)
    required_documents = models.TextField('Required Documents', blank=True)
    url = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class Location(models.Model):
    organization = models.ForeignKey('Organization', verbose_name='Organization', related_name='locations')

    name = models.CharField('Name', max_length=255, blank=True)
    address_1 = models.CharField('Address 1', max_length=255)
    address_2 = models.CharField('Address 2', max_length=255, blank=True)
    city = models.CharField('City', max_length=255)
    country = models.CharField('Country', max_length=255)
    postal_code = models.CharField('Postal Code', max_length=10)
    state_province = models.CharField('State/Province', max_length=2)
    latitude = models.DecimalField('Latitude', max_digits=18, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField('Longitude', max_digits=18, decimal_places=6, blank=True, null=True)
    transportation = models.TextField('Transporation', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class Contact(models.Model):
    organization = models.ForeignKey('Organization', verbose_name='Organization', related_name='contacts')
    service = models.ForeignKey('Service', verbose_name='Primary Service', blank=True, related_name='contacts')
    location = models.ForeignKey('Location', verbose_name='Primary Work Location', blank=True, related_name='contacts')

    email = models.CharField(max_length=255, blank=True)
    name = models.CharField('Full Name', max_length=255)
    title = models.CharField('Title', max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class Hours(models.Model):
    days = (
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday')
    )

    intervals = (
        ('1st', 'First'),
        ('2nd', 'Second'),
        ('3rd', 'Third'),
        ('4th', 'Fourth')
    )

    service = models.ForeignKey('Service', related_name='hours')
    location = models.ForeignKey('Location', related_name='hours')

    opens_at = models.TimeField('Opens at')
    closes_at = models.TimeField('Closes at')
    every = models.CharField('Occurs Every', max_length=255, choices=intervals, blank=True)
    weekday = models.CharField('Weekday', max_length=255, choices=days)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class Phone(models.Model):
    types = (
        ('voice', 'Voice'),
        ('text', 'Text'),
        ('fax', 'Fax'),
        ('tty', 'TTY'),
        ('hotline', 'Hotline')
    )

    contact = models.ForeignKey('Contact', blank=True, related_name="phones")
    organization = models.ForeignKey('Organization', related_name="phones")
    service = models.ForeignKey('Service', blank=True, related_name="phones")

    number = models.CharField(max_length=255)
    primary_phone = models.BooleanField('Organization\'s Primary Phone', default=False)
    extension = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, choices=types)
    vanity_number = models.CharField('Vanity Number', max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class Category(models.Model):
    level = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

class Eligibility(models.Model):
    service = models.ForeignKey('Service', related_name='eligibilities')

    age_range = models.CommaSeparatedIntegerField('Age Range', max_length=7, blank=True)
    disability = models.TextField('Disability', blank=True)
    gender = models.CharField('Gender', max_length=255, blank=True)
    household = models.CharField('Household', max_length=255, blank=True)
    monthly_income_range = models.CommaSeparatedIntegerField('Monthly Income Range', max_length=255, blank=True)
    percent_poverty_range = models.CommaSeparatedIntegerField('Percent Poverty Range', max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class Tag(models.Model):
    level = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
