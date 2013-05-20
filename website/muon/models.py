from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Muon(models.Model):
	user = models.OneToOneField(User,null=True)
	position = models.CharField(max_length="20",null=True)
	name = models.CharField(max_length="30",null=True)
	rank=models.IntegerField(null=True)

	def __unicode__(self):
		return "%s" %self.user.username
