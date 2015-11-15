# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformer', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeggieSailorCousine',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('description', models.TextField(default='')),
                ('parent', models.ForeignKey(null=True, to='vsdata.VeggieSailorCousine')),
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
                ('results_geo_place', models.TextField(blank=True, default='')),
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
                ('content_type', models.ForeignKey(null=True, blank=True, to='contenttypes.ContentType')),
                ('parent', models.ForeignKey(null=True, to='vsdata.VeggieSailorRegion')),
                ('source_region', models.ForeignKey(null=True, unique=True, to='transformer.Region')),
            ],
        ),
        migrations.AddField(
            model_name='veggiesailorentry',
            name='region',
            field=models.ForeignKey(to='vsdata.VeggieSailorRegion'),
        ),
    ]
