# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 23, 59, 20, 120074, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 23, 59, 27, 54073, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eligibility',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 23, 59, 45, 343145, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eligibility',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 23, 59, 48, 87214, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hours',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 23, 59, 49, 654975, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hours',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 23, 59, 51, 39114, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 23, 59, 52, 438992, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 23, 59, 53, 711047, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 23, 59, 55, 222836, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 23, 59, 58, 446632, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 23, 59, 59, 958816, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 0, 0, 2, 262565, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 0, 0, 3, 846719, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 0, 0, 5, 62538, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 0, 0, 6, 110481, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 0, 0, 7, 334532, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
