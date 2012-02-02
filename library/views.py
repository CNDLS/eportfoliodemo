# Create your views here.
import sys

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.models import model_to_dict
from django.http import HttpResponse
from itertools import chain
import operator

from django.contrib.auth.models import User
from eportfoliodemo.profiles.models import UserProfile
from eportfoliodemo.library.models import LibraryState
from eportfoliodemo.libraryitems.models import LibraryItem
from eportfoliodemo.folders.models import Folder
from eportfoliodemo.usercollections.models import Collection
from eportfoliodemo.assets.forms import FileUploadForm

from eportfoliodemo.libraryitems.views import get_librarytree_items_for
from eportfoliodemo.collectionitems.views import get_collectiontree_items_for

from eportfoliodemo.assets.models import Asset, FileType, AssetAlias

from eportfoliodemo.settings import MEDIA_ROOT, AJAX_PREFIX
from present.models import Project

def show(request, user_id):
    requested_user = User.objects.get(pk=user_id)
   	if (request.user.is_authenticated()):
		current_user = User.objects.get(pk=request.user.id)
    
    user_profile, created = UserProfile.objects.get_or_create(user=requested_user)
    if (created):
        user_profile.save
    
    # library_state allows us to return from presentation editing to the library as we left it.
    library_state, created = LibraryState.objects.get_or_create(owner=requested_user)
    
    # get all the folders & assets.
    items_in_library_tree = get_librarytree_items_for(requested_user)
        
    # get all the collections & asset aliases.
    # it's a tree, but without hierarchy (gets us dragging, renaming, etc. parallel to lib).
    items_in_collections_tree = get_collectiontree_items_for(requested_user)

        
    # we'll want to replace this with AJAX call to get current folder contents.
    # think we'll be providing a default root folder for each library, just to keep this simple
    current_assets = Asset.objects.filter(owner=requested_user)
    
    # List of projects on the tabs
    projects = Project.objects.filter(owner=request.user)
    
    file_upload_form = FileUploadForm()
    if request.POST:
        file_type = request.FILES['file'].content_type.split('/')[1]
        asset = Asset()
        asset.owner = request.user
        asset.name = str.replace(str(request.FILES['file']), MEDIA_ROOT, '')
        asset_type, created = FileType.objects.get_or_create(name=file_type)
        asset.file = request.FILES['file']
        asset.size = request.FILES['file'].size
        asset.save()
        asset.filetype.add(asset_type)
        
    return render_to_response('library/show.html',
                    { 'requested_user': requested_user,
                      'current_user': current_user,
                      'current_assets': current_assets,
                      'folder_nodes': items_in_library_tree,
                      'collections_nodes': items_in_collections_tree,
                      'file_upload_form': file_upload_form,
                      'AJAX_PREFIX': AJAX_PREFIX,
                      'projects': projects
                    },
                    context_instance=RequestContext(request))
