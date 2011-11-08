from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<user_id>\d+)/$', 'present.views.show'),
    url(r'^(?P<user_id>\d+)/project/create/$', 'present.views.create_project'),
    url(r'^(?P<user_id>\d+)/project/(?P<project_slug>[-\w]+)/update/$', 'present.views.create_project'),
    url(r'^(?P<user_id>\d+)/public/(?P<project_slug>[-\w]+)/$', 'present.views.display_project')
)

# http://localhost:7000/present/1/project/csc-123-website/update/