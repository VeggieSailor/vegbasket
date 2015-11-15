# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('transformer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeggieSailorCousine',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('description', models.TextField(default='')),
                ('parent', models.ForeignKey(null=True, to='content.VeggieSailorCousine')),
            ],
        ),
        migrations.CreateModel(
            name='VeggieSailorEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=512)),
                ('short_description', models.CharField(default='', max_length=512)),
                ('description', models.TextField(default='')),
                ('address1', models.CharField(default='', max_length=256)),
                ('address2', models.CharField(default='', max_length=256)),
                ('zipcode', models.CharField(default='', max_length=32)),
                ('summary', models.CharField(default='', max_length=512)),
                ('results_geo_place', models.TextField(default='', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'veggie sailor entries',
            },
        ),
        migrations.CreateModel(
            name='VeggieSailorRegion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=512)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', blank=True, null=True)),
                ('parent', models.ForeignKey(null=True, to='content.VeggieSailorRegion')),
                ('source_region', models.ForeignKey(to='transformer.Region', unique=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='veggiesailorentry',
            name='region',
            field=models.ForeignKey(to='content.VeggieSailorRegion'),
        ),
    ]
