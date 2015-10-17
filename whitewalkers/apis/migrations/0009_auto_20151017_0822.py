# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0008_auto_20151017_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='education',
            field=models.TextField(default=b'NA'),
        ),
        migrations.AlterField(
            model_name='user',
            name='interests',
            field=models.TextField(default=b'NA'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profession_type',
            field=models.TextField(default=b'NA'),
        ),
    ]
