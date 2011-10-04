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


def index(request, user_id):
    folders_owner = User.objects.get(pk=user_id)
    folders = Folder.objects.get(owner=folder_owner)
    return render_to_response('folders/index.html', { 'nodes': folders }, context_instance=RequestContext(request))
    
    

def new(request):
    current_user = User.objects.get(pk=request.user.id)
    folder_form = FolderForm(instance=Folder(owner=current_user))

    return render_to_response('folders/new.html', { 'folder_form': folder_form }, context_instance=RequestContext(request))
    

# requires request.method == "POST"
def create(request):
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

    return HttpResponseRedirect(request.META['SCRIPT_NAME'] + '/library/' + str(folder.owner_id))


def update(request, folder_id):
    folder = Folder.objects.get(pk=folder_id)
    for field_name in folder._meta.get_all_field_names():
        # don't need primary key, user, or many-to-many associations
        if request.POST.get(field_name) and (field_name != 'owner') and (field_name != 'parent'):
            setattr(folder, field_name, request.POST.get(field_name))
    folder.save()
    return HttpResponse (folder, mimetype='application/json')


def ajax_rename_folder(request, folder_id):
    if request.is_ajax():
        folder = Folder(pk=folder_id)
        folder.name = request.POST.get("name")
        folder.save()
        return HttpResponse (folder, mimetype='application/json')


def ajax_delete_folder(request, folder_id):
    if request.is_ajax():
        folder = Folder(pk=folder_id)
        folder.delete
        return HttpResponseRedirect(request.META['SCRIPT_NAME'] + '/folders/index' + str(folder.owner_id))