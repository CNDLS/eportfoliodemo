# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from eportfoliodemo.folders.models import Folder, FolderForm


def edit(request):
    current_user = User.objects.get(pk=request.user.id)
    folder, created = Folder.objects.get_or_create(owner=current_user)
    folder_form = FolderForm(instance=folder)

    return render_to_response('folders/edit.html', { 'folder_form': folder_form }, context_instance=RequestContext(request))
    
    

# requires request.method == "POST"
def update(request):
    # make user_profile from post
    folder = Folder.objects.get(owner=request.POST['owner'])
    for field_name in folder._meta.get_all_field_names():
        # don't need primary key, user, or many-to-many associations
        if (field_name != 'id') and (field_name != 'owner') and (field_name[0] != "_"):
            if request.POST.get(field_name):
                setattr(folder, field_name, request.POST.get(field_name))
    folder_form = FolderForm(instance=folder)

    # if folder_form.is_valid():
    folder.save()

    return redirect('/library/' + str(folder.owner_id))