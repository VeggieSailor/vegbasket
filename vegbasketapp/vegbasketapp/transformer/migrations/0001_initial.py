# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('source_id', models.IntegerField(unique=True)),
                ('results_source', models.TextField(blank=True, default='')),
                ('results_geo', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified_source', models.DateTimeField(null=True)),
                ('modified_geo', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('source_id', models.IntegerField(unique=True)),
                ('results_source', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified_source', models.DateTimeField(null=True)),
                ('parent', models.ForeignKey(null=True, to='transformer.Region')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='entry',
            name='region',
            field=models.ForeignKey(to='transformer.Region'),
            preserve_default=True,
        ),
    ]
