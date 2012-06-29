from django.db import models
from django.contrib.auth.models import User

import tagging
from tagging.models import Tag
from tagging.fields import TagField

from eportfoliodemo.settings import PRIVACY
from eportfoliodemo.reflections.models import Reflection
from eportfoliodemo.libraryitems.models import LibraryItem

from eportfoliodemo.mptt.models import MPTTModel


class Folder(LibraryItem):
	name = models.CharField(max_length=255)
	folder_type = models.CharField(max_length=255, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, null=True)
	modified = models.DateTimeField(auto_now=True, null=True)
	privacy = models.CharField(max_length=1, choices=PRIVACY, blank=False, default='1')
	owner = models.ForeignKey(User, blank=False)
	tags = TagField()
	
	def __unicode__(self):
		return self.name

	class MPTTMeta:
		level_attr = 'mptt_level'