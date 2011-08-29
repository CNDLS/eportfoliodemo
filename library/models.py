from django.db import models

from eportfoliodemo.usercollections.models import Collection
from eportfoliodemo.folders.models import Folder


class LibraryState(models.Model):
    selected_folder_item = models.ForeignKey(Folder, blank=True, null=True)
    selected_collection_item = models.ForeignKey(Collection, blank=True, null=True)
    state_meta_area = models.BooleanField()
    
    
