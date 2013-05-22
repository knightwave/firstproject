from django.db import models
from website.muon.models import Muon
from tagging.fields import TagField
from tagging.models import Tag

class Category(models.Model):
	title = models.CharField(max_length=100,null=True)

class Post(models.Model):
	content = models.CharField(max_length=2000, null=True)
	title = models.CharField(max_length=100, null=True)
	author = models.ForeignKey(Muon)
	category = models.ForeignKey(Category, null=True)
	date = models.DateTimeField(auto_now_add=True)
	tags = TagField()
	slug = models.SlugField(unique=True,)
	
	def __unicode__(self):
		return '%s' %self.content
	def get_tags(self):
		return Tag.objects.get_for_object(self) 

class Comment(models.Model):
	post = models.ForeignKey(Post)
	author = models.ForeignKey(Muon)
	content = models.CharField(max_length = 200)
	date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s" %self.content
