from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^(?P<user_id>\d+)/initialize/$', 'dropboxapi.views.initialize', name="dropbox_init"),
	url(r'^(?P<user_id>\d+)/callback/$', 'dropboxapi.views.callback', name="dropbox_callback"),
	# url(r'^authorize/$', 'dropboxapi.views.ajax_dropbox_authorize',name='ajax_dropbox_authorize'),
)