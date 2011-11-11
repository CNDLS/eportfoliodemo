from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Reflection(models.Model):
    content_type = models.ForeignKey(ContentType)
    title = models.CharField(max_length=255, blank=True)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, blank=True) 
    
    def __unicode__(self):
        return self.title
    