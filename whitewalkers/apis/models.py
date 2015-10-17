from django.db import models
from django.contrib.postgres.fields import ArrayField


class Questions(models.Model):
    question_id = models.TextField()
    question_text = models.TextField()
    template_type = models.TextField()
    owner_id = models.TextField()
    profile = models.TextField()
    options = ArrayField(models.TextField(), size=5, default=[])
    flag = models.TextField(default='NA')
    target = models.TextField(default='NA')


class User(models.Model):
    user_id = models.TextField()
    age = models.TextField()
    gender = models.TextField()
    profession_type = models.TextField(default = 'NA')
    interests = models.TextField(default = 'NA')
    education  = models.TextField(default = 'NA')


class Response(models.Model):
    question_id = models.TextField()
    options = models.TextField()
    user_id = models.TextField(default='NA')

class QuestionAndUser(models.Model):
    question_id = models.TextField()
    user_id = models.TextField(default='NA')
