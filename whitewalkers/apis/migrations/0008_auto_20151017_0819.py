# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0007_auto_20151017_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanduser',
            name='user_id',
            field=models.TextField(default=b'abc@xyz.com'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profession_type',
            field=models.TextField(default=b'random'),
        ),
    ]
