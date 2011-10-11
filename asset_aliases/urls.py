from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<asset_alias_id>\d+)/delete/$', 'assets.views.ajax_delete_asset_alias', name='ajax_delete_asset_alias')
)