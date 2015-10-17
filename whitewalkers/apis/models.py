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
    flag = models.TextField()
    target = models.TextField()


class User(models.Model):
    user_id = models.TextField()
    age = models.TextField()
    gender = models.TextField()
    profession_type = models.TextField(default = None)
    interests = models.TextField(default = None)
    education  = models.TextField(default = None)
    # questions_asked = ArrayField(models.TextField(), size=5, default=[])


class Response(models.Model):
    question_id = models.TextField()
    options = models.TextField()
    user_id = models.TextField()

class QuestionAndUser(models.Model):
    question_id = models.TextField()
    user_id = models.TextField()
