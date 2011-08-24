from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'profiles.views.index'),
    (r'^edit/$', 'profiles.views.edit'),
)