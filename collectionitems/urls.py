from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^move/$', 'collectionitems.views.ajax_move_collectionitem', name='ajax_move_collectionitem'),
	url(r'^(?P<owner_id>\d+)/index/$', 'collectionitems.views.index', name='collectionitems_index')
)