from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^new$', 'folders.views.new'),
	url(r'^new/parent/(?P<folder_id>\d+)$', 'folders.views.new_under_parent'),
	url(r'^create/$', 'folders.views.create', name="create_folder"),
	url(r'^(?P<folder_id>\d+)/update/$', 'folders.views.update', name="update_folder"),
	url(r'^(?P<folder_id>\d+)/rename/$', 'folders.views.ajax_rename_folder', name='ajax_rename_folder'),
	url(r'^(?P<folder_id>\d+)/delete/$', 'folders.views.ajax_delete_folder', name='ajax_delete_folder'),
	url(r'^get_folder_items/$', 'folders.views.ajax_get_folder_items', name='ajax_get_folder_items')
)