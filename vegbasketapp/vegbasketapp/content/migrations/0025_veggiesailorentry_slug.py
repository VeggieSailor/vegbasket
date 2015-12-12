# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0024_auto_20151211_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='veggiesailorentry',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='a', populate_from='name', editable=False),
            preserve_default=False,
        ),
    ]
