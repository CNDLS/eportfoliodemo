# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.template import RequestContext
from django.contrib.auth.models import User
from eportfoliodemo.folders.models import Folder
from eportfoliodemo.folders.forms import FolderForm

from eportfoliodemo.snippets.template import render_block_to_string


def new(request):
    current_user = User.objects.get(pk=request.user.id)
    folder_form = FolderForm(instance=Folder(owner=current_user))

    return render_to_response('folders/edit.html', { 'folder_form': folder_form }, context_instance=RequestContext(request))
    
    

# requires request.method == "POST"
def update(request):
    # make user_profile from post
    folder_owner = User.objects.get(pk=request.POST.get("owner"))
    folder = Folder(owner=folder_owner)
    for field_name in folder._meta.get_all_field_names():
        # don't need primary key, user, or many-to-many associations
        if request.POST.get(field_name) and (field_name != 'owner') and (field_name != 'parent'):
            setattr(folder, field_name, request.POST.get(field_name))
            
    # insert folder into tree.
    if request.POST.get("parent"):
        folder.insert_at(Folder.objects.get(pk=request.POST.get("parent")))
    folder_form = FolderForm(instance=folder)

    # if folder_form.is_valid():
    folder.save()

    return redirect('library/' + str(folder.owner_id))
    
    
    
# response to the user dragging and dropping folders.
def move(request, dragged_folder_id, drop_target_id):
    dragged_folder = Folder.objects.get(pk=dragged_folder_id)
    drop_target = Folder.objects.get(pk=drop_target_id)
    Folder.tree.move_node(dragged_folder, drop_target)
    
    folders_owner = User.objects.get(pk=dragged_folder.owner_id)
    folders_in_tree = Folder.tree.get_query_set().filter(owner=folders_owner)
    # return render_to_string ('folders/index.html', { 'nodes': folders_in_tree }, context_instance=RequestContext)
    if request.is_ajax():
        return render_to_response('folders/index.html', { 'nodes': folders_in_tree })
    else:
        return HttpResponseRedirect(request.META['SCRIPT_NAME'] + '/library/' + str(folders_owner.id))
    