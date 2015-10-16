from django.db import models
from django.contrib.postgres.fields import ArrayField


class Questions(models.Model):
    question_id = models.TextField()
    question_text = models.TextField()
    template_type = models.TextField()
    owner_id = models.TextField()
    profile = models.TextField()
    options = ArrayField(models.TextField(), size=5, default=[])


class User(models.Model):
    user_id = models.TextField()
    age = models.TextField()
    gender = models.TextField()
    # questions_asked = ArrayField(models.TextField(), size=5, default=[])


class Response(models.Model):
    question_id = models.TextField()
    options = ArrayField(models.TextField(), size=5, default=[])
