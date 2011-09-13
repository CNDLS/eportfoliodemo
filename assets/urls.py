from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^asset/$', 'assets.views.ajax_get_asset',name='ajax_get_asset'),
    url(r'^metadata/save/$','assets.views.ajax_save_metadata', name='ajax_save_metadata'),
)