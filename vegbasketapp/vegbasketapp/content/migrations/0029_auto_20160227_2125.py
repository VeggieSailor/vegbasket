# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0028_auto_20160227_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='veggiesailorentry',
            name='lat',
            field=models.DecimalField(decimal_places=6, null=True, max_digits=9),
        ),
        migrations.AddField(
            model_name='veggiesailorentry',
            name='long',
            field=models.DecimalField(decimal_places=6, null=True, max_digits=9),
        ),
    ]
