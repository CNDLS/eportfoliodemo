from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<user_id>\d+)/on/(?P<subject_type>[-\w]+)/(?P<subject_id>\d+)$','reflections.views.ajax_create', name='ajax_create_reflection'),
    url(r'^(?P<reflection_id>\d+)/$', 'reflections.views.ajax_show', name='ajax_show_reflection'),
    url(r'^(?P<reflection_id>\d+)/update/$', 'reflections.views.ajax_update', name='ajax_update_reflection'),
    url(r'^(?P<reflection_id>\d+)/delete/$', 'reflections.views.ajax_delete', name='ajax_delete_reflection'),
)user_id