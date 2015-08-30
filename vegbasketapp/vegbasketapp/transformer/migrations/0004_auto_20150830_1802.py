# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('transformer', '0003_auto_20150404_2046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name_plural': 'reviews'},
        ),
        migrations.AddField(
            model_name='entry',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 30, 18, 2, 24, 248614), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 30, 18, 2, 32, 448186), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviews',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 30, 18, 2, 33, 904246), auto_now=True),
            preserve_default=False,
        ),
    ]
