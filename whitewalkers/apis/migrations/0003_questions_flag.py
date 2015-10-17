# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_auto_20151017_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='flag',
            field=models.TextField(default=b'pqr'),
        ),
    ]
