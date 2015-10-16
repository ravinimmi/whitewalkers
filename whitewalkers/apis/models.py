from django.db import models
from djangotoolbox.fields import ListField

# Create your models here.
class Questions(models.Model):
	question_id = models.CharField()
	template_id = models.CharField()
	owner_id = models.CharField()
	profile = models.TextField()

class User(models.Model):
	user_id = models.CharField()
	question_list = models.ListField()
	profile = models.TextField()

class Template(models.Model):
	template_id = models.CharField()
	template_type = models.TextField()

