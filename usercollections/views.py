# Collection views.
from django.shortcuts import render_to_response, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.template import RequestContext
from django.contrib.auth.models import User
from eportfoliodemo.usercollections.models import Collection
from eportfoliodemo.usercollections.forms import CollectionForm

from eportfoliodemo.snippets.template import render_block_to_string


def new(request):
    current_user = User.objects.get(pk=request.user.id)
    collection_form = CollectionForm(instance=Collection(owner=current_user))

    return render_to_response('usercollections/new.html', { 'collection_form': collection_form }, context_instance=RequestContext(request))


    
# requires request.method == "POST"
def create(request):
    # make user_profile from post
    collection_owner = User.objects.get(pk=request.POST.get("owner"))
    collection = Collection(owner=collection_owner)
    for field_name in collection._meta.get_all_field_names():
        # don't need primary key, user, or many-to-many associations
        if request.POST.get(field_name) and (field_name != 'owner') and (field_name != 'parent'):
            setattr(collection, field_name, request.POST.get(field_name))

    collection_form = CollectionForm(instance=collection)

    # if folder_form.is_valid():
    collection.save()

    return HttpResponseRedirect(request.META['SCRIPT_NAME'] + '/library/' + str(collection.owner_id))



# requires request.method == "POST"
def update(request, collection_id):
    # make user_profile from post
    collection_owner = User.objects.get(pk=request.POST.get("owner"))
    collection = Collection.objects.get(pk=collection_id)
    for field_name in collection._meta.get_all_field_names():
        # don't need primary key, user, or many-to-many associations
        if request.POST.get(field_name) and (field_name != 'owner') and (field_name != 'parent'):
            setattr(collection, field_name, request.POST.get(field_name))
            
    collection_form = CollectionForm(instance=collection)

    # if collection_form.is_valid():
    collection.save()

    return HttpResponseRedirect(request.META['SCRIPT_NAME'] + '/library/' + str(collection.owner_id))



def rename(request):    
    try:
        collection_to_rename = Collection.objects.get(pk=request.POST.get("id"))
        collection_to_rename.name = request.POST.get("new_name")
        collection_to_rename.save()
        return HttpResponse('')

    except Exception as exception:
        return HttpResponse(content=exception, status=500)