# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_veggiesailorentry_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='veggiesailorentry',
            name='allows_smoking',
            field=models.NullBooleanField(),
        ),
    ]
