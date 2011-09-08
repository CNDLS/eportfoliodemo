from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^new$', 'folders.views.new'),
    (r'^update/$', 'folders.views.update'),
    (r'^move/(?P<dragged_folder_id>\d+)/(?P<drop_target_id>-?\d+)$', 'folders.views.move')
)