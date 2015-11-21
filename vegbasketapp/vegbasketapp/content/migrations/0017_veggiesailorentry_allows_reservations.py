# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0016_veggiesailorentry_allows_smoking'),
    ]

    operations = [
        migrations.AddField(
            model_name='veggiesailorentry',
            name='allows_reservations',
            field=models.NullBooleanField(),
        ),
    ]
