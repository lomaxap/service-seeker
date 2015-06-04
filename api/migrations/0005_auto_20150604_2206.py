# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150604_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='location',
            field=models.ForeignKey(related_name='contacts', verbose_name=b'Primary Work Location', blank=True, to='api.Location'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='organization',
            field=models.ForeignKey(related_name='contacts', verbose_name=b'Organization', to='api.Organization'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='service',
            field=models.ForeignKey(related_name='contacts', verbose_name=b'Primary Service', blank=True, to='api.Service'),
        ),
        migrations.AlterField(
            model_name='eligibility',
            name='service',
            field=models.ForeignKey(related_name='eligibilities', to='api.Service'),
        ),
        migrations.AlterField(
            model_name='hours',
            name='location',
            field=models.ForeignKey(related_name='hours', to='api.Location'),
        ),
        migrations.AlterField(
            model_name='hours',
            name='service',
            field=models.ForeignKey(related_name='hours', to='api.Service'),
        ),
        migrations.AlterField(
            model_name='location',
            name='organization',
            field=models.ForeignKey(related_name='locations', verbose_name=b'Organization', to='api.Organization'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='contact',
            field=models.ForeignKey(related_name='phones', blank=True, to='api.Contact'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='organization',
            field=models.ForeignKey(related_name='phones', to='api.Organization'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='service',
            field=models.ForeignKey(related_name='phones', blank=True, to='api.Service'),
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(related_name='services', verbose_name=b'Category', to='api.Category'),
        ),
        migrations.AlterField(
            model_name='service',
            name='locations',
            field=models.ManyToManyField(related_name='services', verbose_name=b'Locations', to='api.Location'),
        ),
        migrations.AlterField(
            model_name='service',
            name='organization',
            field=models.ForeignKey(related_name='services', verbose_name=b'Organization', to='api.Organization'),
        ),
        migrations.AlterField(
            model_name='service',
            name='tags',
            field=models.ManyToManyField(related_name='services', verbose_name=b'Tags', to='api.Tag'),
        ),
    ]
