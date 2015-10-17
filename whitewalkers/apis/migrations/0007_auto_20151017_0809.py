# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0006_remove_questions_p'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='user_id',
            field=models.TextField(default=b'abc@xyz.com'),
        ),
    ]
