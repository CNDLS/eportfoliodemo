from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from eportfoliodemo.reflections.models import Reflection
from eportfoliodemo.reflections.forms import ReflectionForm

from datetime import datetime

from eportfoliodemo.settings import MEDIA_ROOT, AJAX_PREFIX

from django.contrib.contenttypes.models import ContentType
from django.core import serializers

from django.contrib.auth.models import User
from eportfoliodemo.assets.models import Asset, AssetAlias


def ajax_new(request, content_type = None, object_id = None):
	form = ReflectionForm(initial={
	'content_type': content_type,
	'object_id': object_id,
	'user_id': request.user.id
	})
	
	obj_array = get_content_type_and_object(content_type, object_id)
	return render_to_response('reflections/edit.html', { 'form': form, 'action': 'create', 'obj':obj_array[1], 'AJAX_PREFIX': AJAX_PREFIX }, context_instance=RequestContext(request))


def ajax_create(request):
	if request.method == "POST":
		reflection = Reflection()
		obj_array = get_content_type_and_object(request.POST["content_type"], request.POST["object_id"])
		
		reflection.author = request.user
		for field_name in ['title','object_id','comment']:
			if (field_name != 'id') and (field_name[0] != "_"):
				setattr(reflection, field_name, request.POST[field_name])
		setattr(reflection, 'content_type', obj_array[0])
		reflection.created = datetime.now()
		reflection.modified = datetime.now()
		reflection.save()
		# return all reflections, so we're always in sync with the whole list for an object
		return ajax_list(request, request.POST["content_type"], request.POST["object_id"])


# list reflections for a selected object
def ajax_list(request, content_type = None, object_id = None):
	obj_array = get_content_type_and_object(content_type, object_id)
	content_type = obj_array[0]
	reflections = Reflection.objects.filter(content_type=content_type, object_id=object_id)
	return render_to_response('reflections/list.html', { 'reflections': reflections, 'AJAX_PREFIX': AJAX_PREFIX }, context_instance=RequestContext(request))
	

def ajax_show(request, reflection_id):
	reflection = Reflection.objects.get(pk=reflection_id)
	return render_to_response('reflections/show.html', { 'reflection': reflection, 'AJAX_PREFIX': AJAX_PREFIX }, context_instance=RequestContext(request))


def ajax_edit(request, reflection_id):
	reflection = Reflection.objects.get(pk=reflection_id)
	form = ReflectionForm(instance=reflection)
	return render_to_response('reflections/edit.html', { 'form': form, 'action': 'edit', 'reflection': reflection, 'obj': reflection.content_object, 'AJAX_PREFIX': AJAX_PREFIX }, context_instance=RequestContext(request))


def ajax_update(request, reflection_id):
	if request.method == "POST":
		reflection = Reflection.objects.get(pk=reflection_id)
		reflection.title = request.POST['title']
		reflection.comment = request.POST['comment']
		reflection.modified = datetime.now()
		reflection.save()
		
		# for editing inline in a project page, just return the reflection
		if (request.POST["context"] == "inline"):
			json_serializer = serializers.get_serializer("json")()
			json_obj = json_serializer.serialize([reflection])
			return HttpResponse(json_obj, mimetype='application/json')
		else:
			# for assets, return all reflections, so we're always in sync with the whole list for an object
			return ajax_list(request, request.POST["content_type"], request.POST["object_id"])

def ajax_delete(request, reflection_id):
	if request.is_ajax():
		reflection = Reflection.objects.get(pk=reflection_id)
		content_type = reflection.content_type
		object_id = reflection.object_id
		reflection.delete()
		return ajax_list(request, content_type, object_id)
	
	
def get_content_type_and_object(content_type = None, object_id = None):
	if (content_type == "asset"):
		app_label = "assets"
	elif (content_type == "assetalias"):
		app_label = "assets"
	elif (content_type == "collection"):
		app_label = "usercollections"
	elif (content_type == "reflection"):
		app_label = "reflections"
	else:
		app_label = "unknown"
		
	reflectedOnType = ContentType.objects.get(app_label=app_label, model=content_type)
	return [reflectedOnType, reflectedOnType.get_object_for_this_type(id=object_id)]
