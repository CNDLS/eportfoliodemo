from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core import serializers
from django.utils import simplejson
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from eportfoliodemo.assets.models import Asset, CustomMetaData, FileType
from eportfoliodemo.assets.forms import MetaDataForm, TagForm
from eportfoliodemo.settings import MEDIA_ROOT

import tagging
from tagging.models import Tag

from eportfoliodemo.libraryitems.views import get_tree_items_for


def ajax_create_asset(request):
    if request.method == "POST":
        file_type = request.FILES['file'].content_type.split('/')[1]
        asset = Asset()
        asset.owner = request.user
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
    asset = Asset.objects.get(id=requested_asset)
    related_meta_data = asset.custom_meta_data.all()
    asset_details = {}
    asset_details['asset'] = json_serializer.serialize([asset])
    asset_details['related_meta_data'] = json_serializer.serialize(related_meta_data)
    asset_details = simplejson.dumps(asset_details)
    return HttpResponse (asset_details, mimetype='application/json')

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

def ajax_save_asset_tags(request):
    form = TagForm()

    asset_update = Asset.objects.get(id=request.GET['asset'])
    
    tags_list = request.GET['tags'].split(',')

    # Process tags
    try:
        tag_list = [x.strip() for x in request.GET['tags'].split(',')]
        for tag in tag_list:
            if tag != '':
                Tag.objects.add_tag(asset_update, '"' + tag + '"')
    except:
        pass
    
    asset_tags = Tag.objects.usage_for_model(Asset, filters=dict(id=asset_update.id))
    json_serializer = serializers.get_serializer("json")()
    asset_tags = json_serializer.serialize(asset_tags)
    return HttpResponse(asset_tags, mimetype='application/json')

def ajax_rename_asset(request, asset_id):
    if request.is_ajax():
        try:
            asset = Asset.objects.get(pk=asset_id)
            asset.name = request.POST.get("name")
            asset.save()
            json_serializer = serializers.get_serializer("json")()
            return HttpResponse (json_serializer.serialize([asset]), mimetype='application/json')

        except Exception as exception:
            return HttpResponse(content=exception, status=500)


def ajax_delete_asset(request, asset_id):
    if request.is_ajax():
        asset = Asset.objects.get(pk=asset_id)
        asset_owner_id = asset.owner_id
        asset.delete()
        return HttpResponseRedirect(reverse('libraryitems_index', args=[asset_owner_id]))