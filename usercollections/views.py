# Collection views.
from django.shortcuts import render_to_response, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.core import serializers
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.models import User
from eportfoliodemo.usercollections.models import Collection
from eportfoliodemo.usercollections.forms import CollectionForm

from eportfoliodemo.snippets.template import render_block_to_string


def new(request):
   	if (request.user.is_authenticated()):
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

	# if collection_form.is_valid():
   	collection.save()

	# return HttpResponseRedirect(request.META['SCRIPT_NAME'] + '/library/' + str(collection.owner_id))
   	json_serializer = serializers.get_serializer("json")()
   	return HttpResponse (json_serializer.serialize([collection]), mimetype='application/json')

def edit(request, collection_id):
	collection = Collection.objects.get(pk=collection_id)
	collection_form = CollectionForm(instance=collection)
	return render_to_response('usercollections/edit.html', { 'collection_form': collection_form, 'collection_id': collection_id }, context_instance=RequestContext(request))
	

# requires request.method == "POST"
def update(request, collection_id):
   	collection_owner = User.objects.get(pk=request.POST.get("owner"))
   	collection = Collection.objects.get(pk=collection_id)
   	for field_name in collection._meta.get_all_field_names():
		# don't need primary key, user, or many-to-many associations
   	   	if request.POST.get(field_name) and (field_name != 'owner') and (field_name != 'parent'):
   	   	   	setattr(collection, field_name, request.POST.get(field_name))
			
   	collection_form = CollectionForm(instance=collection)

	# if collection_form.is_valid():
   	collection.save()

	# return a json object that we update on the page.
	json_serializer = serializers.get_serializer("json")()
	collection = json_serializer.serialize([collection])
	return HttpResponse (collection, mimetype='application/json')
	
   	# return HttpResponseRedirect(request.META['SCRIPT_NAME'] + '/library/' + str(collection.owner_id))



def ajax_rename_collection(request, collection_id):
   	if request.is_ajax():
   	   	try:
			collection = Collection.objects.get(pk=collection_id)
			collection.name = request.POST.get("name")
			collection.save()
			json_serializer = serializers.get_serializer("json")()
			return HttpResponse (json_serializer.serialize([collection]), mimetype='application/json')

		except Exception as exception:
			return HttpResponse(content=exception, status=500)


def ajax_delete_collection(request, collection_id):
	if request.is_ajax():
		collection = Collection.objects.get(pk=collection_id)
		collection_owner_id = collection.owner_id
		collection.delete()
		return HttpResponseRedirect(reverse('collectionitems_index', args=[collection_owner_id]))