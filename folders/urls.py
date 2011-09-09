from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^new$', 'eportfoliodemo.folders.views.new'),
    (r'^update/$', 'eportfoliodemo.folders.views.update'),
    (r'^move/(?P<dragged_folder_id>\d+)/(?P<drop_target_id>-?\d+)$', 'eportfoliodemo.folders.views.move')
)