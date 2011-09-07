from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<user_id>\d+)$', 'folders.views.show'),
    (r'^new$', 'folders.views.new'),
    (r'^update/$', 'folders.views.update'),
    (r'^move/(?P<dragged_folder_id>\d+)/(?P<drop_folder_id>\d+)$', 'folders.views.move')
)