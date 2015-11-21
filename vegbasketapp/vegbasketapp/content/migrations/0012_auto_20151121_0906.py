# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_auto_20151121_0749'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeggieSailorCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='veggiesailorentry',
            name='categories',
            field=models.ManyToManyField(to='content.VeggieSailorCategory'),
        ),
    ]
