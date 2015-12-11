# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0023_auto_20151211_2109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veggiesailorentry',
            old_name='raiting',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='veggiesailorentry',
            old_name='raiting_count',
            new_name='rating_count',
        ),
    ]
