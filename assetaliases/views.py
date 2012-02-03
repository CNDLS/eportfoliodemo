from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core import serializers
from django.utils import simplejson
from eportfoliodemo.assets.models import Asset, AssetAlias


def ajax_delete_asset_alias(request, asset_id):
	if request.is_ajax():
		asset_alias = AssetAlias.objects.get(pk=asset_alias_id)
		asset_alias_owner_id = asset_alias.asset.owner_id
		asset_alias.delete()
		return HttpResponseRedirect(reverse('collectionitems_index', args=[asset_alias_owner_id]))