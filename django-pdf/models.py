from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from tagging.fields imoprt TagField
tagfield_help_text = _('Separate tags with spaces, put quotes around multiple-word tags.')

def get_media_upload_to(instance, filename):
	"""
	A simple way to return the full path	  
	"""
	return 'documents/' + filename
	#return('documents/' + str(instance.type.name) + str(instance.upload_date.year) + '/'
	#	   + str(instance.date.month) + '/' + filename)

class Type(models.Model):
	'''
	Different document subject types.
	'''
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.name

class Document(models.Model):
	title = models.CharField(max_length=100)
	file = models.FileField(upload_to='documents/')
	type = models.ForeignKey(Type)
	user = models.ForeignKey(User)
	upload_date = models.DateTimeField(auto_now_add=True)
	tags = TagField(verbose_name=_('tags'), help_text=tagfield_help_text)
	
	author = models.CharField(blank=True, max_length=100)
	
	def __unicode__(self):
		return self.title
	