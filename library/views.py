# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.models import model_to_dict
from django.http import HttpResponse

from django.contrib.auth.models import User
from eportfoliodemo.library.models import LibraryState
from eportfoliodemo.folders.models import Folder
from eportfoliodemo.usercollections.models import Collection


def show(request, user_id):
    current_user = User.objects.get(pk=request.user.id)
    requested_user = User.objects.get(pk=user_id)
    
    # library_state allows us to return from presentation editing to the library as we left it.
    library_state, created = LibraryState.objects.get_or_create(owner=requested_user)
    
    try:
        folders = Folder.objects.get(owner=requested_user)
        child_folders = Folder.tree.add_related_count(folders.get_children())
    except:
        folders = []
        
    try:
        collections = Collection.objects.get(owner=requested_user)
    except:
        collections = []
        
    return render_to_response('library/show.html', \
                    { 'requested_user': requested_user, \
                      'current_user': current_user, \
                      'folders': folders, \
                      'collections': collections, \
                    },\
                    context_instance=RequestContext(request))