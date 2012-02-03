from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'eportfoliodemo.home.views.index'),
	# (r'^(?P<user_id>\d+)$', 'eportfoliodemo.profiles.views.show'),
	# (r'^(?P<user_id>\d+)/edit/$', 'eportfoliodemo.profiles.views.edit'),
	# (r'^(?P<user_id>\d+)/update/$', 'eportfoliodemo.profiles.views.update'),
)