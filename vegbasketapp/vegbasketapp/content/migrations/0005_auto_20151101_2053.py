# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('content', '0004_auto_20151101_1833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='veggiesailorentry',
            options={'verbose_name_plural': 'veggie sailor entries'},
        ),
        migrations.AddField(
            model_name='veggiesailorentry',
            name='content_type',
            field=models.ForeignKey(to='contenttypes.ContentType', default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='veggiesailorentry',
            name='object_id',
            field=models.PositiveIntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='veggiesailorregion',
            name='content_type',
            field=models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='veggiesailorregion',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
