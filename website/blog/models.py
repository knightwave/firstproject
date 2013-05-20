from django.db import models
from website.muon.models import Muon

class Category(models.Model):
	title = models.CharField(max_length=100,null=True)

class Post(models.Model):
	content = models.CharField(max_length=2000, null=True)
	title = models.CharField(max_length=100, null=True)
	author = models.ForeignKey(Muon)
	category = models.ForeignKey(Category, null=True)
	date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return '%s' %self.content

class Comment(models.Model):
	post = models.ForeignKey(Post)
	author = models.ForeignKey(Muon)
	content = models.CharField(max_length = 200)
	date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s" %self.content
