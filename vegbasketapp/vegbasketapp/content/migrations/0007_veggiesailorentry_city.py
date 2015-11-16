# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20151113_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='veggiesailorentry',
            name='city',
            field=models.CharField(max_length=256, default=''),
        ),
    ]
