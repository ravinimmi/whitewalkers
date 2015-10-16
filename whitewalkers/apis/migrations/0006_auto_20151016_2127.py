# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_auto_20151016_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='option_1',
        ),
        migrations.RemoveField(
            model_name='response',
            name='option_2',
        ),
        migrations.RemoveField(
            model_name='response',
            name='option_3',
        ),
        migrations.RemoveField(
            model_name='response',
            name='option_4',
        ),
        migrations.RemoveField(
            model_name='response',
            name='option_5',
        ),
        migrations.AddField(
            model_name='response',
            name='options',
            field=django.contrib.postgres.fields.ArrayField(default=[], base_field=models.TextField(), size=5),
        ),
    ]
