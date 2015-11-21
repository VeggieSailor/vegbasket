# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_auto_20151121_0906'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeggieSailorCuisine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(default='', max_length=128)),
                ('description', models.TextField(default='')),
                ('parent', models.ForeignKey(null=True, to='content.VeggieSailorCuisine')),
            ],
        ),
        migrations.RemoveField(
            model_name='veggiesailorcousine',
            name='parent',
        ),
        migrations.DeleteModel(
            name='VeggieSailorCousine',
        ),
        migrations.AddField(
            model_name='veggiesailorentry',
            name='cuisines',
            field=models.ManyToManyField(to='content.VeggieSailorCuisine'),
        ),
    ]
