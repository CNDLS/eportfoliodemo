from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'on/(?P<content_type>[-\w]+)/(?P<object_id>\d+)$','reflections.views.ajax_new', name='ajax_new_reflection'),
    url(r'for/(?P<content_type>[-\w]+)/(?P<object_id>\d+)$','reflections.views.ajax_list', name='ajax_list_reflections'),
    url(r'create','reflections.views.ajax_create', name='ajax_create_reflection'),
    url(r'^(?P<reflection_id>\d+)/$', 'reflections.views.ajax_show', name='ajax_show_reflection'),
    url(r'^(?P<reflection_id>\d+)/update/$', 'reflections.views.ajax_update', name='ajax_update_reflection'),
    url(r'^(?P<reflection_id>\d+)/delete/$', 'reflections.views.ajax_delete', name='ajax_delete_reflection')
)