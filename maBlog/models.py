from django.db import models

# Create your models here.
class posts(models.Model):
	post = models.CharField(max_length=200)
	summary = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	date = models.DateTimeField('date published')
	title = models.CharField(max_length=50)




