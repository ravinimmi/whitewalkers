# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_questions_flag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='flag',
        ),
    ]
