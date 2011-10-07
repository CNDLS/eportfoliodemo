from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^asset/$', 'assets.views.ajax_get_asset',name='ajax_get_asset'),
    url(r'^metadata/save/$','assets.views.ajax_save_metadata', name='ajax_save_metadata'),
    url(r'^ajax/create/$','assets.views.ajax_create_asset', name='ajax_create_asset'),
    url(r'^(?P<asset_id>\d+)/rename/$', 'assets.views.ajax_rename_asset', name='ajax_rename_asset'),
    url(r'^(?P<asset_id>\d+)/delete/$', 'assets.views.ajax_delete_asset', name='ajax_delete_asset'),
    url(r'^(?P<asset_id>\d+)/create_alias_in/(?P<collection_id>\d+)$', 'assets.views.ajax_create_alias_in', name='ajax_create_alias_in')
)