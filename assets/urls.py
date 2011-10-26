from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^asset/$', 'assets.views.ajax_get_asset',name='ajax_get_asset'),
    url(r'^metadata/save/$','assets.views.ajax_save_metadata', name='ajax_save_metadata'),
    url(r'^metadata/autocomplete/$','assets.views.ajax_metadata_autocomplete', name='ajax_metadata_autocomplete'),
    url(r'tags/save/$', 'assets.views.ajax_save_asset_tags', name='ajax_save_asset_tags'),
    url(r'tags/delete/$', 'assets.views.ajax_delete_asset_tags', name='ajax_delete_asset_tags'),
    url(r'^ajax/create/$','assets.views.ajax_create_asset', name='ajax_create_asset'),
    url(r'^ajax/update/$','assets.views.ajax_update_asset', name='ajax_update_asset'),
    url(r'file_type/', 'assets.views.ajax_get_file_type', name='ajax_get_file_type'),
    url(r'^(?P<asset_id>\d+)/rename/$', 'assets.views.ajax_rename_asset', name='ajax_rename_asset'),
    url(r'^(?P<asset_id>\d+)/delete/$', 'assets.views.ajax_delete_asset', name='ajax_delete_asset'),
    url(r'^(?P<asset_id>\d+)/create_alias_in/(?P<collection_id>\d+)$', 'assets.views.ajax_create_alias_in', name='ajax_create_alias_in')
)
