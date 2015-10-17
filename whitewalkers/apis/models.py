from django.db import models
from django.contrib.postgres.fields import ArrayField


class Questions(models.Model):
    question_id = models.TextField()
    question_text = models.TextField()
    template_type = models.TextField()
    owner_id = models.TextField()
    profile = models.TextField()
    options = ArrayField(models.TextField(), size=5, default=[])
    #should we make it text field
    flag = models.TextField(default='abc')
    target = models.TextField(default=None)


class User(models.Model):
    user_id = models.TextField()
    age = models.TextField()
    gender = models.TextField()
    profession_type = models.TextField(default = 'NA')
    interests = models.TextField(default = 'NA')
    education  = models.TextField(default = 'NA')
    # questions_asked = ArrayField(models.TextField(), size=5, default=[])


class Response(models.Model):
    question_id = models.TextField()
    options = models.TextField()
    user_id = models.TextField(default='abc@xyz.com')

class QuestionAndUser(models.Model):
    question_id = models.TextField()
    user_id = models.TextField(default='abc@xyz.com')
