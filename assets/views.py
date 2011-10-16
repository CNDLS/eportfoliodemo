# Asset views
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
from tagging.models import TaggedItem

#from eportfoliodemo.libraryitems.views import get_tree_items_for

from eportfoliodemo.assets.models import Asset, AssetAlias, CustomMetaData, FileType
from eportfoliodemo.collectionitems.models import CollectionItem
from eportfoliodemo.assets.forms import MetaDataForm
from eportfoliodemo.settings import MEDIA_ROOT

from eportfoliodemo.libraryitems.views import get_librarytree_items_for
from eportfoliodemo.libraryitems.models import LibraryItem


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
        # return HttpResponse (new_asset, mimetype='application/json')
        return HttpResponse (new_asset, mimetype='text/plain')

def ajax_get_asset(request):
    requested_asset = request.GET['asset']
    json_serializer = serializers.get_serializer("json")()
    asset = Asset.objects.get(id=requested_asset)
    related_meta_data = asset.custom_meta_data.all()
    asset_details = {}
    asset_details['asset'] = json_serializer.serialize([asset])
    asset_details['related_meta_data'] = json_serializer.serialize(related_meta_data)
    asset_details['tags'] = json_serializer.serialize(Tag.objects.usage_for_model(Asset, filters=dict(id=asset.id)))
    asset_details = simplejson.dumps(asset_details)
    return HttpResponse (asset_details, mimetype='application/json')

def ajax_update_asset(request):
    if request.is_ajax():
        asset_id = request.GET['asset_id']
        folder_id = request.GET['folder_id']

        asset = LibraryItem.objects.get(id=asset_id)
        folder = LibraryItem.objects.get(id=folder_id)
        asset.move_to(folder, 'first-child')
        json_serializer = serializers.get_serializer("json")()
        new_asset = json_serializer.serialize(Asset.objects.filter(id=asset.id))
        return HttpResponse (new_asset, mimetype='text/plain')



def ajax_get_file_type(request):
    if request.is_ajax:
        filetype = FileType.objects.filter(id=request.GET['filetypeid'][0])
        json_serializer = serializers.get_serializer("json")()
        filetype = json_serializer.serialize(filetype)
        return HttpResponse(filetype, mimetype='application/json')


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
    json_serializer = serializers.get_serializer("json")()
    metadata = json_serializer.serialize([metadata])
    return HttpResponse(metadata, mimetype='application/json')

def ajax_save_asset_tags(request):
    form = TagForm()

    asset_update = Asset.objects.get(id=request.GET['asset'])
    asset_tags = Tag.objects.usage_for_model(Asset, filters=dict(id=asset_update.id))

    #tags_list = request.GET['tags'].split(',')

    # Process tags
    # try:
    #     tag_list = [x.strip() for x in request.GET['tags'].split(',')]
    #     for tag in tag_list:
    #         if tag != '':
    #             if len(asset_tags) == 0:
    #                 Tag.objects.add_tag(asset_update, '"' + tag + '"')
    #             else:
    #                 Tag.objects.update_tags(asset_update, '"' + tag + '"')
    # except:
    #     pass

    tag_list = [x.strip() for x in request.GET['tags'].split(',')]
    for tag in tag_list:
        Tag.objects.add_tag(asset_update, '"' + tag + '"')

    asset_tags = Tag.objects.usage_for_model(Asset, filters=dict(id=asset_update.id))
    json_serializer = serializers.get_serializer("json")()
    asset_tags = json_serializer.serialize(asset_tags)
    return HttpResponse(asset_tags, mimetype='application/json')

def ajax_delete_asset_tags(request):
    if request.is_ajax():
        tag_id = request.GET['tag_id']
        asset_id = request.GET['asset']
        asset_tag = TaggedItem.objects.filter(object_id=asset_id, tag=tag_id)
        asset_tag.delete()

        updated_asset_tags = Tag.objects.usage_for_model(Asset, filters=dict(id=asset_id))
        json_serializer = serializers.get_serializer("json")()
        updated_asset_tags = json_serializer.serialize(updated_asset_tags)
        return HttpResponse(updated_asset_tags, mimetype='application/json')

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
        
        
def ajax_create_alias_in(request, asset_id, collection_id):
    position = int(request.POST.get("position"))
    target_id = int(request.POST.get("target_id"))
    
    if request.is_ajax():
        asset = Asset.objects.get(pk=asset_id)
        asset_owner_id = asset.owner_id
        assetalias = AssetAlias()
        assetalias.asset_id = asset.id
        assetalias.collection_id = collection_id
        assetalias.save()
        
        try:
            drop_target = CollectionItem.objects.get(pk=target_id)
            prev_siblings = list(drop_target.get_children()[0:position])
            prev_sibling = prev_siblings.pop() if (len(prev_siblings)) else None

            # two moves. first, we move into the target space, defaulting to 'first-child'. 
            # then we move relative to the target.
            assetalias.move_to(drop_target, 'first-child')
                
        except Exception as exception:
            return HttpResponse(content=exception, status=500)
        
        json_serializer = serializers.get_serializer("json")()
        return HttpResponse (json_serializer.serialize([assetalias]), mimetype='application/json')
        

def ajax_delete_assetalias(request, assetalias_id):
    if request.is_ajax():
        assetalias = AssetAlias.objects.get(pk=assetalias_id)
        asset_owner_id = assetalias.asset.owner_id
        assetalias.delete()
        return HttpResponseRedirect(reverse('libraryitems_index', args=[asset_owner_id]))
