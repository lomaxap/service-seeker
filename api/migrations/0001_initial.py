# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=255, blank=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Full Name')),
                ('title', models.CharField(max_length=255, verbose_name=b'Title')),
            ],
        ),
        migrations.CreateModel(
            name='Eligibility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age_range', models.CommaSeparatedIntegerField(max_length=7, verbose_name=b'Age Range', blank=True)),
                ('disability', models.TextField(verbose_name=b'Disability', blank=True)),
                ('gender', models.CharField(max_length=255, verbose_name=b'Gender', blank=True)),
                ('household', models.CharField(max_length=255, verbose_name=b'Household', blank=True)),
                ('monthly_income_range', models.CommaSeparatedIntegerField(max_length=255, verbose_name=b'Monthly Income Range', blank=True)),
                ('percent_poverty_range', models.CommaSeparatedIntegerField(max_length=255, verbose_name=b'Percent Poverty Range', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opens_at', models.TimeField(verbose_name=b'Opens at')),
                ('closes_at', models.TimeField(verbose_name=b'Closes at')),
                ('every', models.CharField(blank=True, max_length=255, verbose_name=b'Occurs Every', choices=[(b'1st', b'First'), (b'2nd', b'Second'), (b'3rd', b'Third'), (b'4th', b'Fourth')])),
                ('weekday', models.CharField(max_length=255, verbose_name=b'Weekday', choices=[(b'mon', b'Monday'), (b'tue', b'Tuesday'), (b'wed', b'Wednesday'), (b'thu', b'Thursday'), (b'fri', b'Friday'), (b'sat', b'Saturday'), (b'sun', b'Sunday')])),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name', blank=True)),
                ('address_1', models.CharField(max_length=255, verbose_name=b'Address 1')),
                ('address_2', models.CharField(max_length=255, verbose_name=b'Address 2', blank=True)),
                ('city', models.CharField(max_length=255, verbose_name=b'City')),
                ('country', models.CharField(max_length=255, verbose_name=b'Country')),
                ('postal_code', models.CharField(max_length=10, verbose_name=b'Postal Code')),
                ('state_province', models.CharField(max_length=2, verbose_name=b'State/Province')),
                ('latitude', models.DecimalField(verbose_name=b'Latitude', max_digits=18, decimal_places=6, blank=True)),
                ('longitude', models.DecimalField(verbose_name=b'Longitude', max_digits=18, decimal_places=6, blank=True)),
                ('transportation', models.TextField(verbose_name=b'Transporation', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
                ('email', models.CharField(max_length=255, blank=True)),
                ('url', models.CharField(max_length=255, blank=True)),
                ('parent_organization', models.ForeignKey(verbose_name=b'Parent Organization', blank=True, to='api.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=255)),
                ('primary_phone', models.BooleanField(default=False, verbose_name=b"Organization's Primary Phone")),
                ('extension', models.CharField(max_length=255, blank=True)),
                ('type', models.CharField(max_length=255, choices=[(b'voice', b'Voice'), (b'text', b'Text'), (b'fax', b'Fax'), (b'tty', b'TTY'), (b'hotline', b'Hotline')])),
                ('vanity_number', models.CharField(max_length=255, verbose_name=b'Vanity Number', blank=True)),
                ('contact', models.ForeignKey(to='api.Contact', blank=True)),
                ('organization', models.ForeignKey(to='api.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Name')),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
                ('application_process', models.TextField(verbose_name=b'Appication Process', blank=True)),
                ('required_documents', models.TextField(verbose_name=b'Required Documents', blank=True)),
                ('url', models.CharField(max_length=255, blank=True)),
                ('category', models.ForeignKey(verbose_name=b'Category', to='api.Category')),
                ('locations', models.ManyToManyField(to='api.Location', verbose_name=b'Locations')),
                ('organization', models.ForeignKey(verbose_name=b'Organization', blank=True, to='api.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='tags',
            field=models.ManyToManyField(to='api.Tag', verbose_name=b'Tags'),
        ),
        migrations.AddField(
            model_name='phone',
            name='service',
            field=models.ForeignKey(to='api.Service', blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='organization',
            field=models.ForeignKey(verbose_name=b'Organization', to='api.Organization'),
        ),
        migrations.AddField(
            model_name='hours',
            name='location',
            field=models.ForeignKey(to='api.Location'),
        ),
        migrations.AddField(
            model_name='hours',
            name='service',
            field=models.ForeignKey(to='api.Service'),
        ),
        migrations.AddField(
            model_name='eligibility',
            name='service',
            field=models.ForeignKey(to='api.Service'),
        ),
        migrations.AddField(
            model_name='contact',
            name='location',
            field=models.ForeignKey(verbose_name=b'Primary Work Location', blank=True, to='api.Location'),
        ),
        migrations.AddField(
            model_name='contact',
            name='organization',
            field=models.ForeignKey(verbose_name=b'Organization', to='api.Organization'),
        ),
        migrations.AddField(
            model_name='contact',
            name='service',
            field=models.ForeignKey(verbose_name=b'Primary Service', blank=True, to='api.Service'),
        ),
    ]
