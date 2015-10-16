# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_user_questions_asked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='option_1',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='option_2',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='option_3',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='option_4',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='option_5',
        ),
        migrations.RemoveField(
            model_name='user',
            name='questions_asked',
        ),
        migrations.AddField(
            model_name='questions',
            name='options',
            field=django.contrib.postgres.fields.ArrayField(default=[], base_field=models.TextField(), size=5),
        ),
    ]
