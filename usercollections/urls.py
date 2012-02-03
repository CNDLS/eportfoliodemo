from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^new$', 'usercollections.views.new'),
	url(r'^create/$', 'usercollections.views.create', name="create_collection"),
	url(r'^(?P<collection_id>\d+)/update/$', 'usercollections.views.update', name="update_collection"),
	url(r'^(?P<collection_id>\d+)/rename/$', 'usercollections.views.ajax_rename_collection', name='ajax_rename_collection'),
	url(r'^(?P<collection_id>\d+)/delete/$', 'usercollections.views.ajax_delete_collection', name='ajax_delete_collection')
)