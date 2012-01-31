from django.db import models

from eportfoliodemo.settings import PRIVACY, PROJECT_TEMPLATE_LOCATION, PROJECT_TEMPLATE_URL
from django.contrib.auth.models import User
import tagging
from tagging.models import Tag
from tagging.fields import TagField
from assets.models import AssetAlias
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from eportfoliodemo.settings import UPLOAD_PATH

class ProjectType(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
    

class TemplateType(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name   
                
class Template(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # current types are just Project and Page, but with other media formats, there may be others.
    # Project Templates are html fragment files likely to contain HTML5 tags such as header/hgroup, nav, footer, section.sidebar.
    # A section.content tag should be required.
    # Page Templates are likely to contain HTML5 tags such as article, figure, image, and video, distributed in columns
    type = models.ForeignKey(TemplateType, blank=False)
    # build file path & url to the template files from "template_path"
    template_path = models.CharField(max_length=255, blank=True, default = 'basic/')
    # owner is useful for when project templates get customized (copied to new records)
    owner = models.ForeignKey(User, null=True, blank=True)
    # need to be able to list default templates (plus those owned by user?) in template selection form.
    is_default = models.BooleanField(default = False)
    screenshot = models.FileField(blank=True, null=True, upload_to=UPLOAD_PATH+'templates/screenshots')
    

    def __unicode__(self):
        return self.name

class Page(models.Model):
    name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField()
    content = models.TextField(blank=True)
    owner = models.ForeignKey(User, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    privacy = models.CharField(max_length=1, choices=PRIVACY, blank=False, default='1')
    template = models.ForeignKey(Template)
    tags = TagField()

    def __unicode__(self):
        return self.name
  
class Project(models.Model):
    name = models.CharField(max_length=255, blank=False)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, null=True, blank=True)
    privacy = models.CharField(max_length=1, choices=PRIVACY, blank=False, default='1')
    type = models.ForeignKey(ProjectType, blank=False)
    template = models.ForeignKey(Template)
    pages = models.ManyToManyField(Page, blank=True, null=True)
    tags = TagField()

    def __unicode__(self):
        return self.name


# attaches items such as AssetAliases and Reflections to html containers in Project Pages.
# NOTE: in Page Templates, html containers that can hold PageItems should be given an id that is unique on the page.
class PageItem(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    page = models.ForeignKey(Page, blank=False)
    page_section_tag_selector = models.CharField(max_length=64, blank=True)
    ordinal = models.PositiveIntegerField() # for when multiple items occupy an html container.

    def __unicode__(self):
        return str(self.content_type.model_class()) + ' for ' + self.page_section_tag_selector + ' on ' + self.page.name
