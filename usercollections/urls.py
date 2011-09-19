from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^new$', 'eportfoliodemo.usercollections.views.new'),
    (r'^update/$', 'eportfoliodemo.usercollections.views.update')
)