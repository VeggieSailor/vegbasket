# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('source_id', models.IntegerField(unique=True)),
                ('results_source', models.TextField(default='', blank=True)),
                ('results_geo', models.TextField(default='', blank=True)),
                ('results_geo_place', models.TextField(default='', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('modified_source', models.DateTimeField(null=True)),
                ('modified_geo', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('source_id', models.IntegerField(unique=True)),
                ('results_source', models.TextField(default='', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('modified_source', models.DateTimeField(null=True)),
                ('parent', models.ForeignKey(to='transformer.Region', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('source_id', models.IntegerField(unique=True)),
                ('results_source', models.TextField(default='', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('modified_source', models.DateTimeField(null=True)),
                ('entry', models.ForeignKey(unique=True, to='transformer.Entry')),
            ],
            options={
                'verbose_name_plural': 'reviews',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='region',
            field=models.ForeignKey(to='transformer.Region'),
        ),
    ]
