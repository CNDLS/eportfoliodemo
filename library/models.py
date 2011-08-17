from django.db import models
from django.contrib.auth.models import User

from usercollections.models import Collection
from folders.models import Folder

class UserProfile(models.Model):
    title = models.TextField(blank=True)
    address = models.TextField(blank=True)
    work_phone = models.CharField(max_length=20, blank=True)
    cell_phone = models.CharField(max_length=20, blank=True)
    alternate_email_1 = models.EmailField(blank=True)
    bio = models.TextField(blank=True)
    web = models.URLField(blank=True, verify_exists=False)
    user = models.ForeignKey(User, unique=True)
    
    def __unicode__(self):
        return self.name

class LibraryState(models.Model):
    selected_folder_item = models.ForeignKey(Folder, blank=True, null=True)
    selected_collection_item = models.ForeignKey(Collection, blank=True, null=True)
    state_meta_area = models.BooleanField()
    
    
