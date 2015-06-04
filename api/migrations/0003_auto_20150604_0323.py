# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150526_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='parent_organization',
            field=models.ForeignKey(verbose_name=b'Parent Organization', to='api.Organization', null=True),
        ),
    ]
