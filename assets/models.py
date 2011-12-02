from django.db import models
from settings import UPLOAD_PATH, PRIVACY
from django.contrib.auth.models import User
import tagging
from tagging.models import Tag
from tagging.fields import TagField

from eportfoliodemo.folders.models import Folder
from eportfoliodemo.reflections.models import Reflection
from eportfoliodemo.libraryitems.models import LibraryItem
from eportfoliodemo.collectionitems.models import CollectionItem

from eportfoliodemo.mptt.models import MPTTModel


class FileType(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name


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
    
    def __unicode__(self):
        return self.name

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