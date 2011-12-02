from django.db import models

from eportfoliodemo.settings import PRIVACY, PROJECT_TEMPLATE_LOCATION, PROJECT_TEMPLATE_URL
from django.contrib.auth.models import User
import tagging
from tagging.models import Tag
from tagging.fields import TagField
from assets.models import AssetAlias

class Page(models.Model):
    name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField()
    content = models.TextField(blank=True)
    owner = models.ForeignKey(User, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    privacy = models.CharField(max_length=1, choices=PRIVACY, blank=False, default='1')
    items = models.ManyToManyField(AssetAlias, blank=True, null=True)
    tags = TagField()

    def __unicode__(self):
        return self.name



class Template(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    template_folder = models.CharField(max_length=255, blank=True, default = PROJECT_TEMPLATE_LOCATION+'basic/') #Path to the theme files
    template_url = models.CharField(max_length=255, blank=True, default = PROJECT_TEMPLATE_URL+'basic/')
    owner = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.name

class ProjectType(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, null=True, blank=True)
    privacy = models.CharField(max_length=1, choices=PRIVACY, blank=False, default='1')
    type = ProjectType(ProjectType)
    template = models.ForeignKey(Template)
    pages = models.ManyToManyField(Page, blank=True, null=True)
    tags = TagField()

    def __unicode__(self):
        return self.name