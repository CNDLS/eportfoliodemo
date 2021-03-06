from django.db import models

from eportfoliodemo.mptt.models import MPTTModel, TreeForeignKey # (v 0.5)

class LibraryItem(MPTTModel):	
	parent = TreeForeignKey('self', null=True, blank=True)
	#name = models.CharField(max_length=255, blank=True)

	def klass( self ):
		return self.__class__.__name__

	def __unicode__(self):
		return self.name   


	class MPTTMeta:
		level_attr = 'mptt_level'