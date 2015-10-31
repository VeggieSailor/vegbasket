# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transformer', '0004_auto_20150830_1802'),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veggiesailorregion',
            name='source_region',
            field=models.ForeignKey(null=True, to='transformer.Region'),
        ),
    ]
