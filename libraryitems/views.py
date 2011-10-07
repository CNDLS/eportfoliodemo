# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.core import serializers

from django.contrib.auth.models import User

from eportfoliodemo.libraryitems.models import LibraryItem
from eportfoliodemo.assets.models import Asset
from eportfoliodemo.folders.models import Folder
from itertools import chain



def index(request, owner_id):
    items_owner = User.objects.get(pk=owner_id)
    return render_to_response('libraryitems/index.html', { 'folder_nodes': get_librarytree_items_for(items_owner) }, context_instance=RequestContext(request))
    
    
# response to the user dragging and dropping folders and assets.
def ajax_move_libraryitem(request):
    dragged_item = LibraryItem.objects.get(pk=int(request.POST.get("id")))
    position = int(request.POST.get("position"))
    target_id = int(request.POST.get("target_id"))
    
    try:
        if (target_id == -1):
            dragged_item.move_to(None, 'left' if (position == 0) else 'right')
            return HttpResponse('')
        else:
            drop_target = LibraryItem.objects.get(pk=target_id)
            prev_siblings = list(drop_target.get_children()[0:position])
            prev_sibling = prev_siblings.pop() if (len(prev_siblings)) else None

            # two moves. first, we move into the target space, defaulting to 'first-child'. 
            # then we move relative to the target.
            dragged_item.move_to(drop_target, 'first-child')
            
            # if ((prev_sibling != None) and (prev_sibling != dragged_item)):
            #     dragged_item.move_to(prev_sibling, 'right')

            return HttpResponse('')
            
    except Exception as exception:
        return HttpResponse(content=exception, status=500)
        
        
        
        
def get_librarytree_items_for(user):
    folders_in_tree = Folder.tree.filter(owner=user)
    assets_in_tree = Asset.tree.filter(owner=user)
    items_in_tree = chain(folders_in_tree, assets_in_tree)
    return sorted(items_in_tree, key=lambda item: (item.tree_id, item.lft))