from django.db import models
from django.forms import ModelForm

from eportfoliodemo.mptt.models import MPTTModel, TreeForeignKey # (v 0.5)


class CollectionItem(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True)
    
    
    class MPTTMeta:
        level_attr = 'mptt_level'