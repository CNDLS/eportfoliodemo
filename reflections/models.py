from django.db import models
from django.contrib.auth.models import User

class Reflection(models.Model):
    title = models.CharField(max_length=255, blank=True)
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, blank=True)
    
    def __unicode__(self):
        return self.title
    