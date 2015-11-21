# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_veggiesailorentry_vs_object_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veggiesailorentry',
            old_name='vs_object_id',
            new_name='vg_object_id',
        ),
    ]
