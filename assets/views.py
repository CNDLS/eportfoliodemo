from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core import serializers

from django.contrib.auth.models import User
from eportfoliodemo.assets.models import Asset, CustomMetaData, FileType
from eportfoliodemo.assets.forms import MetaDataForm
from eportfoliodemo.settings import MEDIA_ROOT

def ajax_create_asset(request):
    if request.method == "POST":
        file_type = request.FILES['file'].content_type.split('/')[1]
        asset = Asset()
        asset.author = request.user
        asset.name = str.replace(str(request.FILES['file']), MEDIA_ROOT, '')
        asset_type, created = FileType.objects.get_or_create(name=file_type)
        asset.file = request.FILES['file']
        asset.size = request.FILES['file'].size
        asset.save()
        asset.filetype.add(asset_type)
        json_serializer = serializers.get_serializer("json")()
        new_asset = json_serializer.serialize(Asset.objects.filter(id=asset.id))
        return HttpResponse (new_asset, mimetype='application/json')

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
    