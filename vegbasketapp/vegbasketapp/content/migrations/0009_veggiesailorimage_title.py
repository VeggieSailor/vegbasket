# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_veggiesailorimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='veggiesailorimage',
            name='title',
            field=models.CharField(default='', max_length=256),
        ),
    ]
