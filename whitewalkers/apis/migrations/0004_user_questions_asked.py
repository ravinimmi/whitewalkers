# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='questions_asked',
            field=django.contrib.postgres.fields.ArrayField(default=[], base_field=models.TextField(), size=5),
        ),
    ]
