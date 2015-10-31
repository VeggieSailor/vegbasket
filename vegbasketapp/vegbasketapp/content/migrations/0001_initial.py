# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VeggieSailorEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(default='', max_length=512)),
                ('summary', models.CharField(default='', max_length=512)),
                ('description', models.TextField(default='')),
                ('results_geo_place', models.TextField(default='', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VeggieSailorRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(default='', max_length=512)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(to='content.VeggieSailorRegion', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='veggiesailorentry',
            name='region',
            field=models.ForeignKey(to='content.VeggieSailorRegion'),
        ),
    ]
