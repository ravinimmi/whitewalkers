# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='flag',
        ),
        migrations.AddField(
            model_name='questions',
            name='profile_flag',
            field=models.TextField(default=b'abc'),
        ),
    ]
