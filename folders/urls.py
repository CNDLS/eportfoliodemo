from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^new$', 'folders.views.edit'),
    (r'^update/$', 'folders.views.update')
)