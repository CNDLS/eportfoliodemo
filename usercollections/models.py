from django.db import models
from django.contrib.auth.models import User

import tagging
from tagging.models import Tag
from tagging.fields import TagField

from eportfoliodemo.settings import PRIVACY
from eportfoliodemo.reflections.models import Reflection
from eportfoliodemo.collectionitems.models import CollectionItem


class Collection(CollectionItem):
	name = models.CharField(max_length=255, blank=True)
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	privacy = models.CharField(max_length=1, choices=PRIVACY, blank=False, default='1')
	owner = models.ForeignKey(User, null=True, blank=True)
	reflections = models.ManyToManyField(Reflection, blank=True, null=True)
	tags = TagField()
	
	def __unicode__(self):
		return self.name

	def klass( self ):
		return self.__class__.__name__
		
		
	def save(self, *args, **kwargs):
		self.parent_id = None
		super(Collection, self).save(*args, **kwargs) # Call the "real" save() method.
				

	class MPTTMeta:
		level_attr = 'mptt_level'