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
    url(r'^(?P<user_id>\d+)/project/(?P<project_id>[-\w]+)/pages/get/(?P<page_id>\d+)/$', 'present.views.get_page_content', name='get_page_content'),
    url(r'^(?P<user_id>\d+)/project/(?P<project_id>[-\w]+)/pages/edit/(?P<page_id>\d+)/$', 'present.views.edit_page_content', name='edit_page'), url(r'^(?P<user_id>\d+)/add/(?P<content_type>[-\w]+)/(?P<object_id>\d+)/to/(?P<project_slug>[-\w]+)/pg/(?P<page_id>\d+)$', 'present.views.add_content'),
)


