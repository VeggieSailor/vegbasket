# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0026_auto_20151212_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeggieSailorOpeningHour',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('from_hour', models.TimeField(null=True)),
                ('duration', models.DurationField(null=True)),
                ('weekday', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('entry', models.ForeignKey(to='content.VeggieSailorEntry')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='veggiesailoropeninghour',
            unique_together=set([('entry', 'from_hour', 'weekday', 'is_closed')]),
        ),
    ]
