from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<user_id>\d+)/$', 'present.views.show'),
    url(r'^(?P<user_id>\d+)/project/create/$', 'present.views.create_project'),
    url(r'^(?P<user_id>\d+)/project/(?P<project_slug>[-\w]+)/update/$', 'present.views.create_project'),
    url(r'^(?P<user_id>\d+)/project/(?P<project_slug>[-\w]+)/compose/$', 'present.views.compose_project', name='compose_project'),
    url(r'^(?P<user_id>\d+)/public/(?P<project_slug>[-\w]+)/$', 'present.views.display_project', name='display_project'),
    url(r'^(?P<user_id>\d+)/public/(?P<project_slug>[-\w]+)/$', 'present.views.project_in_template', name='project_in_template'),
    url(r'^(?P<user_id>\d+)/(?P<project_slug>[-\w]+)/compose/$', 'present.views.compose_project'),
    url(r'^(?P<user_id>\d+)/project/(?P<project_slug>[-\w]+)/pages/add/$', 'present.views.add_page'),
    url(r'^(?P<user_id>\d+)/add/(?P<content_type>[-\w]+)/(?P<object_id>\d+)/to/(?P<project_slug>[-\w]+)/pg/(?P<pg_nbr>\d+)$', 'present.views.add_content'),
)