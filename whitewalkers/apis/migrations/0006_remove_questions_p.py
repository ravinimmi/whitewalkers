# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_auto_20151017_0752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='p',
        ),
    ]
