from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from eportfoliodemo.reflections.models import Reflection
from eportfoliodemo.reflections.forms import ReflectionForm
from datetime import datetime

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
    
    if (content_type == "asset"):
        app_label = "assets"
    elif (content_type == "assetalias"):
        app_label = "assets"
    
    reflectedOnType = ContentType.objects.get(app_label=app_label, model=content_type)
    obj = reflectedOnType.get_object_for_this_type(id=object_id)
    
    return render_to_response('reflections/edit.html', { 'form': form, 'obj':obj }, context_instance=RequestContext(request))


def ajax_create(request):
    if request.method == "POST":
        reflection = Reflection()
        content_type = request.POST["content_type"]
        if (content_type == "asset"):
            app_label = "assets"
        elif (content_type == "assetalias"):
            app_label = "assets"
        
        reflection.content_type = ContentType.objects.get(app_label=app_label, model=content_type)
        reflection.author = request.user
        for field_name in ['title','object_id','comment']:
            if (field_name != 'id') and (field_name[0] != "_"):
                setattr(reflection, field_name, request.POST[field_name])
        reflection.created = datetime.now()
        reflection.modified = datetime.now()
        reflection.save()
        json_serializer = serializers.get_serializer("json")()
        new_reflection = json_serializer.serialize(Reflection.objects.filter(id=reflection.id))
        return HttpResponse(new_reflection, mimetype='text/plain')

def ajax_show(request, reflection_id):
    form = ReflectionForm(instance=Reflection.objects.get(pk=reflection_id))
    return render_to_response('reflections/edit.html', { 'form': form }, context_instance=RequestContext(request))


def ajax_update(request, reflection_id):
    form = ReflectionForm(instance=Reflection.objects.get(pk=reflection_id))
    return render_to_response('reflections/edit.html', { 'form': form }, context_instance=RequestContext(request))


def ajax_delete(request, reflection_id):
    form = ReflectionForm(instance=Reflection.objects.get(pk=reflection_id))
    return render_to_response('reflections/edit.html', { 'form': form }, context_instance=RequestContext(request))