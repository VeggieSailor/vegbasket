# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0020_auto_20151121_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veggiesailorentry',
            name='level',
            field=models.IntegerField(default=0, choices=[(0, 'Not Veg-Friendly'), (1, 'Vegetarian-Friendly'), (2, 'Vegan-Friendly'), (3, 'Vegetarian (But Not Vegan-Friendly)'), (4, 'Vegetarian'), (5, 'Vegan')]),
        ),
        migrations.AlterField(
            model_name='veggiesailorentry',
            name='price',
            field=models.IntegerField(default=0, choices=[(0, 'Unknown'), (1, 'Inexpensive'), (2, 'Average'), (3, 'Expensive')]),
        ),
    ]
