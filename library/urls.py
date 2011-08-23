from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'library.views.index'),
)