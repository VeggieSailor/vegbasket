# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0019_veggiesailorentry_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='veggiesailorentry',
            name='price',
            field=models.IntegerField(choices=[('0', 'Unknown'), ('1', 'Inexpensive'), ('2', 'Average'), ('3', 'Expensive')], default=0),
        ),
        migrations.AlterField(
            model_name='veggiesailorentry',
            name='level',
            field=models.IntegerField(choices=[('0', 'Not Veg-Friendly'), ('1', 'Vegetarian-Friendly'), ('2', 'Vegan-Friendly'), ('3', 'Vegetarian (But Not Vegan-Friendly)'), ('4', 'Vegetarian'), ('5', 'Vegan')], default=0),
        ),
    ]
