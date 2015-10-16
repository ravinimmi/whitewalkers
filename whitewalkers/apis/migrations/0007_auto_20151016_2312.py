# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0006_auto_20151016_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='options',
            field=models.TextField(),
        ),
    ]
