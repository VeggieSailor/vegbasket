# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0021_auto_20151121_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='veggiesailorentry',
            name='raiting',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=6),
        ),
        migrations.AddField(
            model_name='veggiesailorentry',
            name='raiting_count',
            field=models.IntegerField(default=0),
        ),
    ]
