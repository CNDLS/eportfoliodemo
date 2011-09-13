# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from eportfoliodemo.libraryitems.models import LibraryItem
from eportfoliodemo.folders.models import Folder


# response to the user dragging and dropping folders and assets.
def move(request):
    dragged_item = LibraryItem.objects.get(pk=request.POST.get("id"))
    position = int(request.POST.get("position"))
    target_id = int(request.POST.get("target_id"))
    
    try:
        if (target_id == -1):
            dragged_item.move_to(dragged_item.get_root(), 'left' if (position == 0) else 'right')
            return HttpResponse('')
        else:
            drop_target = Folder.objects.get(pk=target_id)
            prev_siblings = list(drop_target.get_children()[0:position])
            prev_sibling = prev_siblings.pop() if (len(prev_siblings)) else None

            # two moves. first, we move into the target space, defaulting to 'first-child'. 
            # then we move relative to the target.
            dragged_item.move_to(drop_target)
            if (prev_sibling != None):
                dragged_item.move_to(prev_sibling, 'right')
            dragged_item.save()

            return HttpResponse('')
            
    except Exception as exception:
        return HttpResponse(content=exception, status=500)