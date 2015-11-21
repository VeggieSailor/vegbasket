# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_veggiesailortag'),
    ]

    operations = [
        migrations.AddField(
            model_name='veggiesailorentry',
            name='tags',
            field=models.ManyToManyField(to='content.VeggieSailorTag'),
        ),
    ]
