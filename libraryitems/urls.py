from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^move/$', 'eportfoliodemo.libraryitems.views.move')
)