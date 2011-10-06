from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^move/$', 'libraryitems.views.ajax_move_item', name='ajax_move_item'),
    url(r'^(?P<owner_id>\d+)/index/$', 'libraryitems.views.index', name='libraryitems_index'),
)