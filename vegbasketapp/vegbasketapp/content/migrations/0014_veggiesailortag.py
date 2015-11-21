# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_auto_20151121_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeggieSailorTag',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
    ]
