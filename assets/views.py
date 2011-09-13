from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core import serializers

from django.contrib.auth.models import User
from eportfoliodemo.assets.models import Asset, CustomMetaData
from eportfoliodemo.assets.forms import MetaDataForm

def ajax_get_asset(request):
    requested_asset = request.GET['asset']
    json_serializer = serializers.get_serializer("json")()
    asset = json_serializer.serialize(Asset.objects.filter(id=requested_asset))
    return HttpResponse (asset, mimetype='application/json')

def ajax_save_metadata(request):
    form = MetaDataForm()
    
    metadata = CustomMetaData()
    metadata.fieldname = request.GET['fieldname']
    metadata.value = request.GET['value']
    metadata.owner = User.objects.get(username=request.GET['owner'])
    metadata.save()
    
    asset_update = Asset.objects.get(id=request.GET['asset'])
    asset_update.custom_meta_data.add(metadata)
    asset_update.save()
    
    return HttpResponse(metadata, mimetype='application/json')
    