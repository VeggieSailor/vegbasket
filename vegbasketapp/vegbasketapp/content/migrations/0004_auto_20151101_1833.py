# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20150927_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeggieSailorCousine',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, default='')),
                ('description', models.TextField(default='')),
                ('parent', models.ForeignKey(null=True, to='content.VeggieSailorCousine')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='veggiesailorentry',
            name='short_description',
            field=models.CharField(max_length=512, default=''),
            preserve_default=True,
        ),
    ]
