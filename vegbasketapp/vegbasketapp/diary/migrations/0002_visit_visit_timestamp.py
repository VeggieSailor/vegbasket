# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 22:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='visit_timestamp',
            field=models.DateField(default=datetime.datetime(2016, 7, 30, 22, 16, 30, 611343, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
