# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from eportfoliodemo.collectionitems.models import CollectionItem
from eportfoliodemo.folders.models import Folder


# response to the user dragging and dropping folders and assets.
def move(request):
    dragged_item = CollectionItem.objects.get(pk=int(request.POST.get("id")))
    position = int(request.POST.get("position"))
    target_id = int(request.POST.get("target_id"))
    
    try:
        if (target_id == -1):
            dragged_item.move_to(None, 'left' if (position == 0) else 'right')
            return HttpResponse('')
        else:
            drop_target = CollectionItem.objects.get(pk=target_id)
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
        
        

def rename(request):    
    try:
        item_to_rename = CollectionItem.objects.get(pk=request.POST.get("id"))
        item_to_rename.name = request.POST.get("new_name")
        item_to_rename.save()
        return HttpResponse('')
            
    except Exception as exception:
        return HttpResponse(content=exception, status=500)
