from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'profiles.views.index'),
    (r'^(?P<user_id>\d+)$', 'profiles.views.show'),
    (r'^(?P<user_id>\d+)/edit/$', 'profiles.views.edit'),
    (r'^(?P<user_id>\d+)/update/$', 'profiles.views.update'),
)