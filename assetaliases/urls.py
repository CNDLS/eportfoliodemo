from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<assetalias_id>\d+)/delete/$', 'assets.views.ajax_delete_assetalias', name='ajax_delete_assetalias')
)