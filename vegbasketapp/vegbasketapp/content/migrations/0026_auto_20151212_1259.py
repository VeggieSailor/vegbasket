# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0025_veggiesailorentry_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veggiesailorentry',
            name='slug',
            field=models.SlugField(),
        ),
    ]
