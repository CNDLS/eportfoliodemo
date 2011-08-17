from django.db import models
from django.contrib.auth.models import User

from settings import PRIVACY
from assets.models import Asset
from reflections.models import Reflection

class Folder(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    privacy = models.CharField(max_length=1, choices=PRIVACY, blank=False, default='1')
    parent = models.ForeignKey('self', blank=True, null=True)
    assets = models.ManyToManyField(Asset, blank=True, null=True)
    
    def __unicode__(self):
        return self.name