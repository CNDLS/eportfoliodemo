from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^new$', 'eportfoliodemo.folders.views.new'),
    (r'^update/$', 'eportfoliodemo.folders.views.update'),
    (r'^move/$', 'eportfoliodemo.folders.views.move')
)