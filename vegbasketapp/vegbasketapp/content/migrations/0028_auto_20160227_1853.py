# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0027_auto_20160103_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeggieSailorRating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('note', models.TextField(default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('rating', models.IntegerField()),
                ('entry', models.ForeignKey(to='content.VeggieSailorEntry')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='veggiesailoropeninghour',
            options={'ordering': ['weekday', 'from_hour']},
        ),
        migrations.AlterField(
            model_name='veggiesailoropeninghour',
            name='entry',
            field=models.ForeignKey(to='content.VeggieSailorEntry', related_name='opening_hours'),
        ),
        migrations.AlterField(
            model_name='veggiesailorregion',
            name='source_region',
            field=models.OneToOneField(null=True, to='transformer.Region'),
        ),
    ]
