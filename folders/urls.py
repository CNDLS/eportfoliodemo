from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^new$', 'eportfoliodemo.folders.views.new'),
    (r'^new/parent/(?P<folder_id>\d+)$', 'eportfoliodemo.folders.views.new_under_parent'),
    (r'^update/$', 'eportfoliodemo.folders.views.update'),
    url(r'^create/$', 'folders.views.create', name="create_folder"),
    url(r'^(?P<folder_id>\d+)/rename/$', 'folders.views.ajax_rename_folder', name='ajax_rename_folder'),
    url(r'^(?P<folder_id>\d+)/update/$', 'folders.views.update', name="update_folder"),
    url(r'^(?P<folder_id>\d+)/delete/$', 'folders.views.ajax_delete_folder', name='ajax_delete_folder')
)