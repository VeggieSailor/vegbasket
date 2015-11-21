# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0017_veggiesailorentry_allows_reservations'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeggieSailorPayment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='veggiesailorentry',
            name='payments',
            field=models.ManyToManyField(to='content.VeggieSailorPayment'),
        ),
    ]
