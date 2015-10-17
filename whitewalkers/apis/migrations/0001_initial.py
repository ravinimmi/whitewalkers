# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAndUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_id', models.TextField()),
                ('user_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_id', models.TextField()),
                ('question_text', models.TextField()),
                ('template_type', models.TextField()),
                ('owner_id', models.TextField()),
                ('profile', models.TextField()),
                ('options', django.contrib.postgres.fields.ArrayField(default=[], base_field=models.TextField(), size=5)),
                ('flag', models.TextField(default=None)),
                ('target', models.TextField(default=None)),
                ('p', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_id', models.TextField()),
                ('options', models.TextField()),
                ('user_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.TextField()),
                ('age', models.TextField()),
                ('gender', models.TextField()),
                ('profession_type', models.TextField(default=None)),
                ('interests', models.TextField(default=None)),
                ('education', models.TextField(default=None)),
            ],
        ),
    ]
