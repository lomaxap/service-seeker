# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150604_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(null=True, verbose_name=b'Latitude', max_digits=18, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(null=True, verbose_name=b'Longitude', max_digits=18, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='organization',
            field=models.ForeignKey(verbose_name=b'Organization', to='api.Organization'),
        ),
    ]
