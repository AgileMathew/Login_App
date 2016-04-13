from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserDetails(models.Model):
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	mailid = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	
	def __str__(self):              # __unicode__ on Python 2
	        return self.firstname