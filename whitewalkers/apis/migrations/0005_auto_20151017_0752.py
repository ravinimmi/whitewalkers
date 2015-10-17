# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_remove_questions_flag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='profile_flag',
            new_name='flag',
        ),
    ]
