# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0022_auto_20151210_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veggiesailorentry',
            name='raiting',
            field=models.FloatField(default='0.0'),
        ),
    ]
