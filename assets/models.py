from django.db import models
from settings import UPLOAD_PATH, PRIVACY, MEDIA_ROOT, MEDIA_URL
from django.contrib.auth.models import User
import tagging
import os
from tagging.models import Tag
from tagging.fields import TagField

from eportfoliodemo.folders.models import Folder
from eportfoliodemo.reflections.models import Reflection
from eportfoliodemo.libraryitems.models import LibraryItem
from eportfoliodemo.collectionitems.models import CollectionItem

from eportfoliodemo.mptt.models import MPTTModel
from os.path import basename

class FileType(models.Model):
	name = models.CharField(max_length=100)
	icon = models.FileField(upload_to=UPLOAD_PATH+'filetype-icons/', blank=True, null=True)
	
	def __unicode__(self):
		return self.name

	def get_icon_url(self):
		# file_location = MEDIA_ROOT+'uploads/filetype-icons/'
		# file_url = MEDIA_URL+"uploads/filetype-icons/"
		# icon_location = str(self.icon)
		# filename = str.replace(file_location,file_url,icon_location)
		# return str(filename)
		filename = os.path.basename(str(self.icon))
		return MEDIA_URL+"uploads/filetype-icons/"+filename


class CustomMetaData(models.Model):
	fieldname = models.CharField(max_length=255, blank=True)
	value = models.TextField(blank=True)
	owner = models.ForeignKey(User, null=True, blank=True)
	
	def __unicode__(self):
		return self.fieldname


class Asset(LibraryItem):
	name = models.CharField(max_length=255, blank=True)
	description = models.TextField(blank=True)
	file = models.FileField(upload_to=UPLOAD_PATH+'assets/', blank=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	privacy = models.CharField(max_length=1, choices=PRIVACY, blank=False, default='1')
	owner = models.ForeignKey(User, null=True, blank=True)
	size = models.CharField(max_length=10, blank=True)
	filetype = models.ManyToManyField(FileType, blank=True, null=True)
	reflection = models.ManyToManyField(Reflection, blank=True, null=True)
	custom_meta_data = models.ManyToManyField(CustomMetaData, blank=True, null=True)
	tags = TagField()
	html_content = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.name
		
	def url(self):
		return MEDIA_URL+"uploads/assets/"+self.name
		
	def contents(self):
		try:
			fname = os.path.basename(self.file.name)
			if (self.file.name.find(".docx") > -1):
				fname = MEDIA_ROOT+"uploads/assets/"+fname.replace(".docx", "_bogus.html")
			elif (self.file.name.find(".doc") > -1):
				fname = MEDIA_ROOT+"uploads/assets/"+fname.replace(".doc", "_bogus.html")
			elif (self.file.name.find(".png") > -1):
				fname = MEDIA_URL+"uploads/assets/"+fname
				return "<image src='"+ fname +"'></image>"
			else:
				raise Exception("Only provide dummy content for Word files.")
				
			print fname
			f = open(fname)
			return f.read()
		except Exception as exception:
			print exception
			return ""

	class MPTTMeta:
		level_attr = 'mptt_level'
		
		
class AssetAlias(CollectionItem):
	collection = models.ForeignKey('usercollections.Collection', blank=True, null=True)
	reflection = models.ManyToManyField(Reflection, blank=True, null=True)
	asset = models.ForeignKey(Asset, blank=True, null=True)
	
	def name(self):
		return self.asset.name
			
	def __unicode__(self):
		return self.asset.name

	class MPTTMeta:
		level_attr = 'mptt_level'