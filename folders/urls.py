from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^new$', 'eportfoliodemo.folders.views.new'),
    (r'^update/$', 'eportfoliodemo.folders.views.update'),
    url(r'^create/$', 'folders.views.create', name="create_folder"),
    url(r'^(?P<folder_id>\d+)update/$', 'folders.views.update', name="update_folder")
)