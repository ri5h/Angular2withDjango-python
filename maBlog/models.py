from django.db import models

# Cnreate your models here.
class posts(models.Model):
	post = models.CharField(max_length=200)
	summary = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	date = models.DateTimeField('date published')
	title = models.CharField(max_length=50)
	
	def __str__(self):
		return self.summary
	
	def __toDict(self):
		dict = {}
		dict['author'] = self.author
		dict['summary'] = self.summary
		dict['date'] = self.date
		dict['title'] = self.title
		dict['id'] = self.id
		return dict




