# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_veggiesailorregion_source_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veggiesailorregion',
            name='source_region',
            field=models.ForeignKey(unique=True, to='transformer.Region', null=True),
        ),
    ]
