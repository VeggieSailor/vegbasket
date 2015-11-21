# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_veggiesailorimage_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='veggiesailorentry',
            name='vs_object_id',
            field=models.IntegerField(null=True),
        ),
    ]
