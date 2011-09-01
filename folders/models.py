from django.db import models
from django.contrib.auth.models import User

import tagging
from tagging.models import Tag
from tagging.fields import TagField

from eportfoliodemo.settings import PRIVACY
from eportfoliodemo.assets.models import Asset
from eportfoliodemo.reflections.models import Reflection

from eportfoliodemo.mptt.models import MPTTModel #, TreeForeignKey (wait for v 0.5)


class Folder(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    privacy = models.CharField(max_length=1, choices=PRIVACY, blank=False, default='1')
    parent = models.ForeignKey('self', null=True, blank=True)
    owner = models.ForeignKey(User, blank=False)
    assets = models.ManyToManyField(Asset, blank=True, null=True)
    tags = TagField()
    
    def __unicode__(self):
        return self.name
        
        
    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by=['name']
        

