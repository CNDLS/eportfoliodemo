# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.models import model_to_dict
from django.http import HttpResponse
from itertools import chain
import operator

from django.contrib.auth.models import User
from eportfoliodemo.library.models import LibraryState
from eportfoliodemo.libraryitems.models import LibraryItem
from eportfoliodemo.folders.models import Folder
from eportfoliodemo.usercollections.models import Collection
from eportfoliodemo.assets.forms import FileUploadForm

from eportfoliodemo.assets.models import Asset, FileType, AssetAlias

from eportfoliodemo.settings import MEDIA_ROOT


def show(request, user_id):
    requested_user = User.objects.get(pk=user_id)
    current_user = User.objects.get(pk=request.user.id)
    
    # library_state allows us to return from presentation editing to the library as we left it.
    library_state, created = LibraryState.objects.get_or_create(owner=requested_user)
    
    # get all the folders & assets.
    folders_in_tree = Folder.tree.filter(owner=requested_user)
    assets_in_tree = Asset.tree.filter(author=request.user)
    items_in_tree = chain(folders_in_tree, assets_in_tree)
    items_in_tree = sorted(items_in_tree, key=lambda item: (item.tree_id, item.lft))
        
    # get all the collections & asset aliases.
    # it's a tree, but without hierarchy (gets us dragging, renaming, etc. parallel to lib).
    collections_in_tree = Collection.tree.filter(owner=requested_user)
    asset_aliases_in_tree = AssetAlias.tree.filter(asset__author=request.user)
    collection_items_in_tree = chain(collections_in_tree, asset_aliases_in_tree)
    collection_items_in_tree = sorted(collection_items_in_tree, key=lambda item: (item.tree_id, item.lft))

        
    # we'll want to replace this with AJAX call to get current folder contents.
    # think we'll be providing a default root folder for each library, just to keep this simple
    current_assets = Asset.objects.filter(author=requested_user)
    
    
    file_upload_form = FileUploadForm()
    if request.POST:
        file_type = request.FILES['file'].content_type.split('/')[1]
        asset = Asset()
        asset.author = request.user
        asset.name = str.replace(str(request.FILES['file']), MEDIA_ROOT, '')
        asset_type, created = FileType.objects.get_or_create(name=file_type)
        asset.file = request.FILES['file']
        
        asset.save()
        asset.filetype.add(asset_type)
        
    return render_to_response('library/show.html',
                    { 'requested_user': requested_user,
                      'current_user': current_user,
                      'current_assets': current_assets,
                      'folder_nodes': items_in_tree,
                      'collections_nodes': collection_items_in_tree,
                      'file_upload_form': file_upload_form
                    },
                    context_instance=RequestContext(request))
