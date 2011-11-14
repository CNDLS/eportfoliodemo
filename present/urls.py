from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<user_id>\d+)/$', 'present.views.show'),
    url(r'^(?P<user_id>\d+)/project/create/$', 'present.views.create_project'),
    url(r'^(?P<user_id>\d+)/project/(?P<project_slug>[-\w]+)/update/$', 'present.views.create_project'),
    url(r'^(?P<user_id>\d+)/public/(?P<project_slug>[-\w]+)/$', 'present.views.display_project'),
    url(r'^(?P<user_id>\d+)/project/(?P<project_slug>[-\w]+)/pages/add/$', 'present.views.add_page'),
)

# {{request.META.SCRIPT_NAME}}/present/{{request.user.id}}/project/{{project.slug}}/update/