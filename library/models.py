from django.db import models
from django.contrib.auth.models import User


class LibraryState(models.Model):
	selected_tree_item = models.ForeignKey('libraryitems.LibraryItem', blank=True, null=True)
	selected_collection = models.ForeignKey('usercollections.Collection', blank=True, null=True)
	selected_collection_item = models.ForeignKey('assets.AssetAlias', blank=True, null=True)
	state_meta_area = models.BooleanField()
	owner = models.ForeignKey(User, unique=True)