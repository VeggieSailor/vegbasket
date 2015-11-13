# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20151101_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='veggiesailorentry',
            name='address1',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='veggiesailorentry',
            name='address2',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='veggiesailorentry',
            name='zipcode',
            field=models.CharField(default='', max_length=32),
        ),
    ]
