# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_veggiesailorentry_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeggieSailorImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('photo', models.ImageField(width_field='width', upload_to='entries/photos', height_field='height')),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('entry', models.ForeignKey(to='content.VeggieSailorEntry')),
            ],
        ),
    ]
