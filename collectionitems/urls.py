from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^move/$', 'eportfoliodemo.collectionitems.views.move'),
    (r'^rename/$', 'eportfoliodemo.collectionitems.views.rename')
)