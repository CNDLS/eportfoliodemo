# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template.loader import render_to_string
from django.utils import simplejson
from django.template import RequestContext
from django.contrib.auth.models import User
from eportfoliodemo.folders.models import Folder, FolderForm

from eportfoliodemo.snippets.template import render_block_to_string


def show(request, user_id):
    requested_user = User.objects.get(pk=user_id)
    
    # json = simplejson.dumps(list(folders_in_tree))
    # return HttpResponse(json, mimetype='application/json')
    
    # will use this with jsTree jQuery plugin to manipulate folder relationships
    folders_in_tree = Folder.tree.get_query_set().filter(owner=requested_user)
    return render_block_to_string('library/show', 'folder_tree', { 'nodes': folders_in_tree }, context_instance=RequestContext)
    
    # return render_to_string('folders/tree.json', { 'tree': folders_in_tree }) #  , context_instance=RequestContext)
    # return render_to_response('folders/index.html', { 'nodes': folders_in_tree }, context_instance=RequestContext(request))


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
        if request.POST.get(field_name) and (field_name != 'owner'):
            setattr(folder, field_name, request.POST.get(field_name))
    folder_form = FolderForm(instance=folder)

    # if folder_form.is_valid():
    folder.save()

    return redirect('/library/' + str(folder.owner_id))